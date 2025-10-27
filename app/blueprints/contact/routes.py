from flask import render_template

from . import contact_bp
from .forms import ContactForm


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Handle form submission here
        # For now, just pass - you can add email sending logic later
        pass

    return render_template("contact/contact.html", form=form)
