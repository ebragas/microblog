from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eric'} # NOTE: placeholder
    posts = [
        {'author': {'username': 'John'}, 'body': 'God I love Sundays'},
        {'author': {'username': 'Eric'}, 'body': 'I love getting to do these kinds of things'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
