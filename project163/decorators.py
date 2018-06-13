from functools import wraps
from flask import url_for, session, redirect


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
