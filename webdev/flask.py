from flask import Flask, rendertemplate, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'index'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/links')
def links():
    return '<a href = "{}"> Index </a>'.format(url_for('index'))