from flask import render_template

from . import shop_bp


@shop_bp.route("/shop")
def shop():
    return render_template("shop/shop.html")
