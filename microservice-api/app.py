from flask import Flask, request
from Models import db, Usuario
from service import create_task, save_task_request, get_task_by_id, delete_task_by_id, process_task_by_id, save_user
import json
import hashlib

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

    password1 = request.json["password1"]
    password2 = request.json["password2"]

    if len(password1)>0 and len(password2)>0 and password1==password2:
        usuario = Usuario.query.filter(Usuario.usuario == request.json["username"]).first()
        correo = Usuario.query.filter(Usuario.correo == request.json["email"]).first()
        if usuario is None and correo is None:
           return save_user(request)
        else:
            return "El username y/o email ya existe",404   
    else: 
        return "El  password no coincide",404

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
        return delete_task_by_id(id_task)
    else:
        return get_task_by_id(id_task)
    
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

@app.route('/process-task/<id_task>', methods = ['POST'])
def process_task(id_task):
    process_task_by_id(id_task)
    message = {
        "status": 0,
        "message": "Task {} se empieza a procesar en la base de datos".format(id_task) 
    }
    return json.dumps(message), 200

with app.app_context():
    db.create_all()