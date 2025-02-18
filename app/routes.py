from flask import Blueprint, render_template, request, jsonify
from app.jsonld_generator import generate_jsonld

jsonld_routes = Blueprint("jsonld", __name__)

@jsonld_routes.route("/preview", methods=["GET"])
def preview():
    return render_template("index.html")

@jsonld_routes.route("/generate-jsonld", methods=["POST"])
def generate_jsonld_route():
    data = request.json
    content_type = data.get("type")
    jsonld = generate_jsonld(content_type, data)
    return jsonify(jsonld)