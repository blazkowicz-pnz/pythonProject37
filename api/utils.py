import json

from config import POSTS

def load_data_from_json(POSTS):
    with open(POSTS, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def load_post_by_id(id):
    posts = load_data_from_json(POSTS)
    for post in posts:
        if post["pk"] == id:
            return post