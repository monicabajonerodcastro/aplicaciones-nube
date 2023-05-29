from Models import Tasks, db
from utils import my_compress_file_GCP
import datetime, json

def process_task_by_id(id):
    message = {
        "status": 0,
        "message" : ""
    }
    status = 200

    task = Tasks.query.get(id)
    if task is not None:
        if task.status == "PROCESSING":
            task.last_time = datetime.datetime.utcnow()
            db.session.commit()
            try:
                result_path = my_compress_file_GCP(file_name=task.path, new_format=task.format)
                task.status = "PROCESSED"
                task.last_time = datetime.datetime.utcnow()
                task.result_path = result_path
                db.session.commit()
                message["message"] = "Task {} se empieza a procesar".format(id)
            except Exception as e:
                print(e, flush=True)
                task.status = "UPLOADED"
                task.last_time = datetime.datetime.utcnow()
                db.session.commit()
                message["status"] = 1
                message["message"] = "Ocurrio un error al procesar: [{}]".format(e)
                status = 500
        else:
            message["status"] = 1
            message["message"] = "La tarea {} se encuentra en estado {} y no se puede procesar".format(task.id, task.status)
            status = 400
    else:
        message["status"] = 1
        message["message"] = "La tarea {} no se encuentra registrada".format(id)
        status = 404

    return json.dumps(message), status
