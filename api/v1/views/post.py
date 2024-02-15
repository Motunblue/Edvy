#!/usr/bin/python3
""" Post api """
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request, session


@app_views.route('/posts', methods=['GET', 'POST'],
                 strict_slashes=False)
def get_post():
    """ Retive all post
    """
    school_id = request.headers.get('User-Id')
    print(school_id)
    posts_list = []
    posts = storage.get_post(school_id=school_id)
    if not posts:
        abort(404)
    for post in posts:
        posts_list.append(post.to_dict())
    return jsonify(posts_list)
