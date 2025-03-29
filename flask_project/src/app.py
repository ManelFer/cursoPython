from flask import Flask, url_for

app = Flask(__name__)

@app.route("/olamundo")
def hello_world():
    return "<p>Hello, World!</p>"

# definir outra rota
@app.route("/bemvindo")
def wellcome():
    return "<p>bem vindo!</p>"


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'



@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('bemvindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))