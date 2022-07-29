import pytest
from main.utils import load_data_from_json, search_post_by_id, get_comment_by_post_id, get_post_by_user_name, get_posts_by_word, get_posts_by_tag
from config import POSTS


def test_load_json_data():
    data = load_data_from_json(POSTS)
    assert type(data) == list, TypeError


def test_search_post_by_id():
    data = load_data_from_json(POSTS)
    for d in data:
        post = search_post_by_id(d["pk"])
        assert type(post) == dict, TypeError


def test_get_comments():
    data = load_data_from_json(POSTS)
    for d in data:
        commets = get_comment_by_post_id(d["pk"])
        assert type(commets) == list, TypeError


def test_get_posts_by_user_name():
    data = load_data_from_json(POSTS)
    for d in data:
        user_posts = get_post_by_user_name(d["poster_name"])
        assert type(user_posts) == list, TypeError


def test_get_post_by_word():
    posts_list = get_posts_by_word(str)
    assert type(posts_list) == list, TypeError



