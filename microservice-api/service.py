#Import constants
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'constants'))

import uuid, datetime, json
from werkzeug.utils import secure_filename
from Models import db, Tasks, TasksSchema, Usuario
from utils import publish_message, compress_local_file
from flask_jwt_extended import create_access_token
import hashlib
from constants import UPLOAD_FOLDER 


task_schema = TasksSchema()

def create_task(request):
    message = {
        "status": 0,
        "message" : ""
    }
    status = 200

    if "file" not in request.files:
        message["status"] = 1
        message["message"] = "No se encontró el archivo"
        status = 404
    else:
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            message["status"] = 1
            message["message"] = "No se encontró el archivo"
            status = 404
        
        else:
            filename = secure_filename(uploaded_file.filename)

            id_task = str(uuid.uuid4())
            path = os.path.join(UPLOAD_FOLDER, filename)
            format_task = request.form['format']

            message_to_publish = {
                "id" : id_task,
                "path" : path,
                "format" : format_task
            }
            
            publish_message(queue="requests_queue", message=message_to_publish)
            uploaded_file.save(path)

            message["status"] = 0
            message["message"] = "Tarea creada exitosamente con el id {}".format(id_task)
            status = 200

    return json.dumps(message), status

def save_task_request(request):
    id_task = request.json['id']
    format_task = request.json['format']
    path = request.json['path']

    time_now = datetime.datetime.utcnow()
    new_task = Tasks(id=id_task, path=path, status="UPLOADED", time=time_now, format=format_task, last_time=time_now)
    db.session.add(new_task)
    db.session.commit()

def get_task_by_id(id):
    task = Tasks.query.get(id)
    if task is None:
        message = {
            "status" : 1,
            "message" : "La tarea con el id {} no se encuentra registrada".format(id)
        }
        return json.dumps(message), 404
    return task_schema.dump(task)

def delete_task_by_id(id):
    task = Tasks.query.get(id)
    if task is None:
        message = {
            "status" : 1,
            "message" : "La tarea con el id {} no se encuentra registrada".format(id)
        }
        return json.dumps(message), 404
    
    db.session.delete(task)
    db.session.commit()
    message = {
        "status" : 0,
        "message" : "La tarea con el id {} fue eliminada exitosamente".format(id)
    }
    return json.dumps(message)

def process_task_by_id(id):
    task = Tasks.query.get(id)
    if task is not None:
        if task.status == "PROCESSING":
            task.last_time = datetime.datetime.utcnow()
            db.session.commit()
            try:
                result_path = compress_local_file(task.path)
                task.status = "PROCESSED"
                task.last_time = datetime.datetime.utcnow()
                task.result_path = result_path
                db.session.commit()
            except:
                task.status = "UPLOADED"
                task.last_time = datetime.datetime.utcnow()
                db.session.commit()
        else:
            print("La tarea {} se encuentra en estado {} y no se puede procesar".format(task.id, task.status), flush=True)

def publish_uploaded_tasks():
    tasks = Tasks.query.filter_by(status='UPLOADED')
    count = 0
    for task in tasks:
        message_to_publish = {
            "id" : task.id
        }
        publish_message(queue="processes_queue", message=message_to_publish)
        task.status = 'PROCESSING'
        db.session.commit()
        count += 1

    message = {
        "status" : 0,
        "count" : count
    }
    return message

def save_user(request):
    contrasena_encriptada = hashlib.md5(request.json["password1"].encode('utf-8')).hexdigest()
    nuevo_usuario = Usuario(usuario=request.json["username"], contrasena=contrasena_encriptada,correo=request.json["email"])
    db.session.add(nuevo_usuario)
    db.session.commit()   
    return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id} 

def login_user(request):
    contrasena_encriptada = hashlib.md5(request.json["password"].encode('utf-8')).hexdigest()
    usuario = Usuario.query.filter(Usuario.usuario == request.json["username"],
                                    Usuario.contrasena == contrasena_encriptada).first()
    db.session.commit()
    if usuario is None:
        return "El usuario no existe", 404
    else:
        token_de_acceso = create_access_token(identity=usuario.id)
        return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso, "id": usuario.id}        

