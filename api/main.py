## Using the Flask microframework for Python
## Adopt a MVC (Model-View-Controller) Design


from flask import Flask, render_template
from flask_pymongo import PyMongo

from src.models.game import load_game

# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)

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
    if(token==None):
        raise WebError('Please enter a valid token')
    return render_template('game.html', token=token)
