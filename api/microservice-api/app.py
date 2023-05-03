#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

from flask import Flask, request
from Models import db, Usuario
from service import create_task, save_task_request, get_task_by_id, get_tasks, delete_task_by_id, save_user,login_user, publish_uploaded_tasks,get_file_by_task
import json
from flask_jwt_extended import JWTManager,jwt_required

from constants import HOST_POSTGRES

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:secret@{}:5432/application'.format(HOST_POSTGRES)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
app.config['JWT_SECRET_KEY'] = 'frase-secreta'

db.init_app(app)
jwt = JWTManager(app)

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
    return login_user(request)


@app.route('/api/tasks', methods = ['GET', 'POST'])
@jwt_required()
def tasks():
    if request.method == 'POST':
        return create_task(request)
    else:
        return get_tasks(request)


@app.route('/api/tasks/<id_task>', methods = ['GET', 'DELETE'])
@jwt_required()   
def task(id_task):
    if request.method == 'DELETE':
        return delete_task_by_id(id_task)
    else:
        return get_task_by_id(id_task)


@app.route('/api/files/<id_task>')
@jwt_required()   
def filename(id_task):

    return get_file_by_task(id_task)

# Private endpoints
@app.route('/save-task', methods = ['POST'])
def save_task():
    save_task_request(request)
    message = {
        "status": 0,
        "message": "Task creado en la base de datos" 
    }
    return json.dumps(message), 200

@app.route('/publish-pending-tasks')
def publish_pending_tasks():
    return publish_uploaded_tasks()

@app.route('/health-check')
def healt_check():
    return "Status UP"

with app.app_context():
    db.create_all()
    
