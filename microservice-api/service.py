import os, uuid, datetime, json
from werkzeug.utils import secure_filename
from Models import db, Tasks, TasksSchema
from utils import publish_message

UPLOAD_FOLDER = "/Users/mbajonero/Downloads/uploaded-files"
#UPLOAD_FOLDER = "/microservice-api/uploaded-files"

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

    new_task = Tasks(id=id_task, path=path, status="UPLOADED", time=datetime.datetime.utcnow(), format=format_task)
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