from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def main(username=None, post_id=None):
    return render_template('./index.html', username=username, post_id=post_id)

@app.route('/blog/')
def blog():
    return 'blog page'

@app.route('/about/')
def about():
    return render_template('./about.html')