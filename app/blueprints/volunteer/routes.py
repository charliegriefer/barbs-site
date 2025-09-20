from flask import render_template

from . import volunteer_bp


@volunteer_bp.route("/volunteer")
def volunteer():
    return render_template("volunteer/volunteer.html")
