from flask import render_template

from app.services.about.about_service import AboutService

from . import about_bp


@about_bp.route("/about")
def about():
    team_members = AboutService().team_members()
    board_members = AboutService().board_members()
    return render_template(
        "about/about.html", team_members=team_members, board_members=board_members
    )
