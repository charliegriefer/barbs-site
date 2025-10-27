from flask import render_template

from . import volunteer_bp
from .forms import VolunteerForm


@volunteer_bp.route("/volunteer", methods=["GET", "POST"])
def volunteer():
    form = VolunteerForm()

    if form.validate_on_submit():
        # Handle form submission here
        # For now, just pass - you can add email sending logic later
        pass

    return render_template("volunteer/volunteer.html", form=form)
