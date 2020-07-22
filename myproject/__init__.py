import os
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SECRET_KEY'] ='mykey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

from myproject.states.views import state_blueprint
from myproject.politicians.views import politician_blueprint
from myproject.party.views import party_blueprint

app.register_blueprint(state_blueprint,url_prefix='/state')
app.register_blueprint(politician_blueprint,url_prefix='/politician')
app.register_blueprint(party_blueprint,url_prefix='/party')
