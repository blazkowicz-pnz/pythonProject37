from flask import Flask, Blueprint, render_template, jsonify, config
from api.utils import load_data_from_json, load_post_by_id
from config import POSTS

api_blueprint = Blueprint("api_blueprint", __name__, static_folder="static", )


@api_blueprint.route("/api/posts")
def get_json_data():
    try:
        data_json = load_data_from_json(POSTS)
        return jsonify(data_json)
    except FileNotFoundError:
        return "Файл не найден!"


@api_blueprint.route("/api/posts/<int:id>")
def get_post_as_json(id):
    if id <= len(load_data_from_json(POSTS)):
        json_post = load_post_by_id(id)
        return jsonify(json_post)
    return "Пост с таким id не существует"
