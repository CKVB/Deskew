from flask import jsonify


def index():
    return jsonify({"Hello": "World"})