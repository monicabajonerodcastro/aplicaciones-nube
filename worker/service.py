from Models import Tasks, db
from utils import compress_local_file
import datetime


def process_task_by_id(id):
    task = Tasks.query.get(id)
    if task is not None:
        if task.status == "PROCESSING":
            task.last_time = datetime.datetime.utcnow()
            db.session.commit()
            try:
                result_path = compress_local_file(task.path, task.format)
                task.status = "PROCESSED"
                task.last_time = datetime.datetime.utcnow()
                task.result_path = result_path
                db.session.commit()
            except Exception as e:
                print(e, flush=True)
                task.status = "UPLOADED"
                task.last_time = datetime.datetime.utcnow()
                db.session.commit()
        else:
            print("La tarea {} se encuentra en estado {} y no se puede procesar".format(task.id, task.status), flush=True)