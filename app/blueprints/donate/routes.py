from flask import render_template

from . import donate_bp


@donate_bp.route("/donate")
def donate():
    return render_template("donate/donate.html")
