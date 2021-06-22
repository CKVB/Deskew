from flask import Blueprint, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from .routes.getView import get_view


swagger_url_prefix = "/swagger"
swagger_file_path = "/static/swagger_doc.yml"
swagger_ui = get_swaggerui_blueprint(swagger_url_prefix, swagger_file_path)

deskew_api = Blueprint("deskew_api", __name__)


@deskew_api.route("/", methods=["GET"])
def index():
    return redirect("swagger")


@deskew_api.route("/deskew", methods=["POST"])
def deskew_image():
    return get_view("DESKEW")
