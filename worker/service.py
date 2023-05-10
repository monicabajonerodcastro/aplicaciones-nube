from Models import Tasks, db
from utils import my_compress_file_GCP
import datetime


def process_task_by_id(id):
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
                return "Task {} se empieza a procesar en la base de datos".format(id) 
            except Exception as e:
                print(e, flush=True)
                #task.status = "UPLOADED"
                task.last_time = datetime.datetime.utcnow()
                db.session.commit()
                return "Ocurrio un error al procesar la task {}. Error: {}".format(id, e) 
        else:
            return "La tarea {} se encuentra en estado {} y no se puede procesar".format(task.id, task.status)