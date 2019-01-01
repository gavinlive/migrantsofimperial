## Using the Flask microframework for Python
## Adopt a MVC (Model-View-Controller) Design


from flask import Flask, render_template

# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker containers! testing!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

'''
from flask_pymongo import PyMongo

from src.models.game import load_game

from src.lib.authentication import is_valid_game_token

## include db name in URI; _HOST entry overwrites all others
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/settlersofcatan'
app.debug = True
mongo = PyMongo(app)

# global vars: app, mongo

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/game/')
@app.route('/game/<token>')
def load_game(token=None):
    if(token is None or is_valid_game_token(token) is False):
        raise WebError('Please enter a valid token')
    pass

@app.route('/game/<token>/state')
def get_game_state(token=None):
    return render_template('game.html', token=token)

@app.route('/game/<token>/robberposition'):
def get_robber_position(token=None):
    return render_template('robber_position.html', token=token)
'''
