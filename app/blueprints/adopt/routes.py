from flask import render_template

from . import adopt_bp


@adopt_bp.route("/adopt")
def adopt():
    return render_template("adopt/adopt.html")


@adopt_bp.route("/adoption-events")
def adoption_events():
    return render_template("adopt/adoption_events.html")


@adopt_bp.route("/vacation")
def vacation():
    return render_template("adopt/vacation.html")
