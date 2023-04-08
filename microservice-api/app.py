from flask import Flask, request
from Models import db

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Endpoints
@app.route('/api/auth/signup', methods = ['POST'])
def signup():
    return "POST - sign up"

@app.route('/api/auth/login', methods = ['POST'])
def login():
    return "POST - login"

@app.route('/api/tasks', methods = ['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        return "POST - tasks"
    else:
        return "GET - tasks"
    
@app.route('/api/tasks/<id_task>', methods = ['GET', 'DELETE'])
def task(id_task):
    if request.method == 'DELETE':
        return "DELETE - task by id {}".format(id_task)
    else:
        return "GET - task by id {}".format(id_task)
    
@app.route('/api/files/<filename>')
def filename(filename):
    return "GET - filename: {}".format(filename)