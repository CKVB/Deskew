from flask import Blueprint
from .routes.getView import get_view


deskew_api = Blueprint("deskew_api", __name__)


@deskew_api.route("/", methods=["GET"])
def index():
    return get_view("INDEX")


@deskew_api.route("/deskew", methods=["POST"])
def deskew_image():
    return get_view("DESKEW")
