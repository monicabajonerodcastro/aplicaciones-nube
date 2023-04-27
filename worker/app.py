#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

from flask import Flask
from Models import db
from service import process_task_by_id
from constants import HOST_POSTGRES
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:secret@{}:5432/application'.format(HOST_POSTGRES)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

db.init_app(app)

@app.route('/process-task/<id_task>', methods = ['POST'])
def process_task(id_task):
    process_task_by_id(id_task)
    message = {
        "status": 0,
        "message": "Task {} se empieza a procesar en la base de datos".format(id_task) 
    }
    return json.dumps(message), 200