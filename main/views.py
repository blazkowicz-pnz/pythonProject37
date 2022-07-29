from flask import Blueprint, render_template, send_from_directory, request, redirect
from main.utils import load_data_from_json, search_post_by_id, get_comment_by_post_id, get_post_by_user_name, get_posts_by_word, get_posts_by_tag, add_to_bookmarks, remove_post
import config


posts_blueprint = Blueprint("posts_blueprint", __name__, static_folder="static", template_folder="templates")


@posts_blueprint.route("/")
def index_page():
    """ Вывод всех постов """
    data = load_data_from_json(config.POSTS)
    bookmarks_posts = load_data_from_json(config.BOOKMARKS)
    count_bookmarks_posts = len(bookmarks_posts)
    return render_template("index.html", data=data, count_bookmarks_posts=count_bookmarks_posts)


@posts_blueprint.route("/post/<int:id>")
def post_contetn(id):
    """ Вывод поста по ID """
    post = search_post_by_id(id)
    new_post = []
    for p in post["content"].split(" "):
        if p[0] == "#":
            new_p = p.replace(p, f"<a href='/tag/{p[1:]}'>{p}</a>")
        else:
            new_p = p
        new_post.append(new_p)
    post["content"] = " ".join(new_post)
    comments = get_comment_by_post_id(id)
    return render_template("post.html", post=post, comments=comments)


@posts_blueprint.route("/users/<username>")
def user_posts(username):
    """ вывод всех постов пользователя 'username' """
    user_posts = get_post_by_user_name(username)
    return render_template("user-feed.html", user_posts=user_posts)


@posts_blueprint.route("/search/")
def search_posts():
    """ поиск по слову """
    word = request.args.get("word")
    posts = get_posts_by_word(word)
    return render_template("search.html", word=word, posts=posts)


@posts_blueprint.route("/bookmarks/")
def bookmarks_page():
    """ вывод всех закладок """
    bookmarks_posts = load_data_from_json(config.BOOKMARKS)
    count_bookmarks_posts = len(bookmarks_posts)
    return render_template("bookmarks.html", bookmarks_posts=bookmarks_posts , count_bookmarks_posts=count_bookmarks_posts)


@posts_blueprint.route("/tag/<tag_name>")
def tag_page(tag_name):
    """ вывод постов по тэгу """
    posts = get_posts_by_tag(tag_name)
    full_tag = f"#{tag_name}"

    return render_template("tag.html", posts=posts, tag_name=tag_name, full_tag=full_tag)


@posts_blueprint.route("/bookmarks/add/<int:id>")
def post_add_to_bookmarks(id):
    """ добавление поста в закладки, с проверкой на наличие """
    post = search_post_by_id(id)
    all_bookmarks = load_data_from_json(config.BOOKMARKS)
    for b in all_bookmarks:
        if b == post:
            return "Такой пост уже добавлен!"
    add_to_bookmarks(post)
    return redirect("/")


@posts_blueprint.route("/bookmarks/remove/<int:id>")
def del_bookmarks(id):
    """ удаление поста из закладок """
    bookmarks_posts = load_data_from_json(config.BOOKMARKS)
    for post in bookmarks_posts:
        if id == post["pk"]:
            remove_post(post)

    return redirect("/")


@posts_blueprint.route("/img/<path:path>")
def static_dir(path):
    """ открываем доступ к папке IMG """
    return send_from_directory("img", path)
