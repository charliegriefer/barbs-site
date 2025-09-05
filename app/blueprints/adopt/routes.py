from flask import render_template

from . import adopt_bp


@adopt_bp.route("/adopt")
def adopt():
    return render_template("adopt/adopt.html")
