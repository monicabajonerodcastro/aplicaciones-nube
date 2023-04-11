from flask import Flask, request
from Models import db
from service import create_task, save_task_request
import json

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

db.init_app(app)

# Public Endpoints
@app.route('/api/auth/signup', methods = ['POST'])
def signup():
    return "POST - sign up"

@app.route('/api/auth/login', methods = ['POST'])
def login():
    return "POST - login"

@app.route('/api/tasks', methods = ['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        return create_task(request)
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

# Private endpoints
@app.route('/save-task', methods = ['POST'])
def save_task():
    save_task_request(request)
    message = {
        "status": 0,
        "message": "Task creado en la base de datos" 
    }
    return json.dumps(message), 200

with app.app_context():
    db.create_all()