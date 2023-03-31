from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '8897860c1796b6de34c14ed06ca0ff2d'

db = SQLAlchemy(app)