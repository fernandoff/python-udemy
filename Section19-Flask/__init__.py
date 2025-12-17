from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
app.config['SECRET_KEY'] = '2f206f88c20d49c35538bf8f'
db.init_app(app)
bcrypt = Bcrypt(app)

from market import routes