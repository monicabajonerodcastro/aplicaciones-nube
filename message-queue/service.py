import requests, json

API_ENDPOINT_SAVE = "http://microservice-api:5003/save-task"
API_ENDPOINT_PROCESS = "http://microservice-api:5003/process-task/{}"
#API_ENDPOINT_SAVE = "http://127.0.0.1:5000/save-task" -> Comentar para Docker. Quitar comentario para local
#API_ENDPOINT_PROCESS = "http://127.0.0.1:5000/process-task/{}" -> Comentar para Docker. Quitar comentario para local

def call_endpoint_save(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    requests.post(url = API_ENDPOINT_SAVE, json=body_json)

def call_endpoint_process(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    requests.post(url = API_ENDPOINT_PROCESS.format(body_json["id"]))