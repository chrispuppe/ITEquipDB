from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Create an Instance of Flask
app = Flask(__name__)
#Include config from config.py
app.config.from_object('config')
app.secret_key = 's4asdgfkjagh2345nnlqnexiIS9732KksdnsdklkLKJjlksdfJLDF02418'
#Create an instance of SQLAclhemy
db = SQLAlchemy(app)
from app import views, models
# (venv)[cpuppe@localhost]$ vim flask-blog/config.py
# #Add your connection string
# SQLALCHEMY_DATABASE_URI = 'mysql://root:ThisTime43@localhost/blog'