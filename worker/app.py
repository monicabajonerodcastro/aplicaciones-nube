from flask import Flask, request
from Models import db
from service import process_task_by_id
from constants import USER_POSTGRES, PASSWORD_POSTGRES, HOST_POSTGRES
import json, base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://{}:{}@{}:5432/application'.format(USER_POSTGRES, PASSWORD_POSTGRES, HOST_POSTGRES)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

db.init_app(app)

@app.route('/process-task', methods = ['POST'])
def process_task():

    json_request = request._get_current_object().get_json()
    encoded_message = json_request.get('message').get("data")
    decoded_message = base64.b64decode(encoded_message).decode("utf-8") 
    data = json.loads(decoded_message)
    id_task = data.get('id')

    return process_task_by_id(id_task)

@app.route('/health-check')
def healt_check():
    return "Status Worker UP"