from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
#from format_date import date_range, single
import os
from dbvars import postgres_uri


app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.environ['FLASK_ENV'] == 'development':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri
else:
    app.debug = False
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)
from models import Person, Truck, Trip


@app.route('/')
def index():
    #return "<h1>Hello, World!</h1>"
    return render_template("index.html",) 


@app.route('/optimize')
def optimize():
    #return "<h1>Hello, World!</h1>"
    return render_template("optimize.html",)

import auth, trucks, trips
app.register_blueprint(auth.bp)
app.register_blueprint(trucks.bp)
app.register_blueprint(trips.bp)

if __name__ == '__main__':
    app.run()