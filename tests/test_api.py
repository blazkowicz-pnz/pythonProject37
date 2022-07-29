from app import app
from api.utils import load_data_from_json, load_post_by_id
from config import POSTS


def test_api():
    response = app.test_client().get("/api/posts")
    assert response.status_code == 200


def test_type_posts():
    data = load_data_from_json(POSTS)
    assert type(data) == list, TypeError



def test_type_post():
    data = load_data_from_json(POSTS)
    for d in data:
        id = int(d["pk"])
        post = load_post_by_id(id)
        assert type(post) == dict, TypeError


def test_keys():
    true_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    response = app.test_client().get("/api/posts")
    for post in response.json:
        for key in true_keys:
            assert (key in post.keys()) == True, KeyError


