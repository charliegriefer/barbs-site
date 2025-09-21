from flask import current_app, render_template, request

from app.extensions import cache
from app.services.adopt.adopt_service import DogService
from app.utils import calculate_page_link

from . import adopt_bp

# Create the service - no fallback will ever be used
dog_service = DogService(cache)


# We'll use an init-app function to load dogs once when the application starts
@adopt_bp.record_once
def on_register(state):
    """Load dogs on first use of the blueprint when app context is available"""
    app = state.app
    with app.app_context():
        try:
            # Try to load dogs once on startup
            dog_service.load_available_dogs()
            current_app.logger.info("Initial dog data loaded on application startup")
        except Exception as e:
            current_app.logger.error(f"Error loading initial dog data: {e}")
            current_app.logger.info("Will attempt to load dog data on first request")


@adopt_bp.route("/adopt")
def adopt_page():
    # Process search request
    search_data = dog_service.process_search_request(request.args)

    # Prepare forms
    search_form, pagination_form = dog_service.prepare_forms(search_data)
    return render_template(
        "adopt/adopt.html",
        search_form=search_form,
        pagination_form=pagination_form,
        calculate_page_link=calculate_page_link,
        **search_data,
    )


@adopt_bp.route("/adopt/results")
def dog_results():
    """
    HTMX endpoint to render only the dog results section.
    This allows for pagination without a full page reload.
    """
    # Process search request
    search_data = dog_service.process_search_request(request.args)

    # Prepare forms
    search_form, pagination_form = dog_service.prepare_forms(search_data)

    # If this is an HTMX request, return only the dog results
    if request.headers.get("HX-Request"):
        return render_template(
            "adopt/_dog_results.html",
            search_form=search_form,
            pagination_form=pagination_form,
            calculate_page_link=calculate_page_link,
            **search_data,
        )

    # If it's a regular request, redirect to the full page
    return adopt_page()


@adopt_bp.route("/dog/<int:dog_id>")
def dog_detail(dog_id):
    dog = dog_service.get_dog_by_id(dog_id)
    return render_template("adopt/dog_detail.html", dog=dog)


@adopt_bp.route("/adoption-events")
def adoption_events():
    return render_template("adopt/adoption_events.html")


@adopt_bp.route("/vacation")
def vacation():
    return render_template("adopt/vacation.html")


@adopt_bp.route("/refresh-dogs")
def refresh_dogs():
    """Force a refresh of dog data"""
    try:
        # Clear the cache first
        cache.delete("available_dogs")
        # Load new data
        dog_service.load_available_dogs()
        dog_count = len(dog_service.get_available_dogs())
        return f"Successfully refreshed dog data. {dog_count} dogs loaded."
    except Exception as e:
        return f"Error refreshing dog data: {str(e)}", 500
