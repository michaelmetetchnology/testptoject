from enum import unique
from operator import concat
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY']='a07cec9805a8d58d3ca8ad2fcee73dc8'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from project import routs