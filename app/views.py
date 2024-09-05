from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def search():
    return render_template('search.html')
