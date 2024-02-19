#!/usr/bin/python3
""" Post api """
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_views.route('/posts', methods=['GET'],
                 strict_slashes=False)
def get_post():
    """ Retive all post
    """
    user_id = request.headers.get('User-Id')
    school_id = request.headers.get('School-Id')
    school_id = user_id if school_id == "null" else school_id
    posts_list = []
    posts = storage.get_post(school_id=school_id)
    if not posts:
        abort(404)
    for post in posts:
        post_dict = post.to_dict()
        if post.student_id:
            by = post.student.to_dict()
            post_dict["by"] = f'{by["first_name"]} {by["last_name"]}'
        elif post.staff_id:
            by = post.staff.to_dict()
            post_dict["by"] = f'{by["first_name"]} {by["last_name"]}'
        else:
            by = post.school.to_dict()
            post_dict["by"] = by.get("name")
        posts_list.append(post_dict)
    return jsonify(posts_list)
