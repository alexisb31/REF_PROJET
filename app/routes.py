from flask import Blueprint, render_template


jsonld_routes = Blueprint("jsonld", __name__)

@jsonld_routes.route("/preview", methods=["GET"])
def preview():
    
    return render_template("index.html")
