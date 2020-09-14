from flask import Flask,render_template,Response
app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add_user')
def add_user():
    return Response('........')

@app.route('/user_list')
def user_list():
    return Response('........')


@app.route('/add_user')
def add_user():
    return Response('........')

@app.route('/user_list')
def user_list():
    return Response('........')

@app.route('/add_user')
def add_user():
    return Response('........')

@app.route('/user_list')
def user_list():
    return Response('........')
if __name__ == '__main__':
    app.run()