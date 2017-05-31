from flask import Flask
import flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 123 World'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hah.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
