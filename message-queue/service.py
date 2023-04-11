import requests, json

#API_ENDPOINT = "http://microservice-api:5003/save-task"
API_ENDPOINT = "http://127.0.0.1:5000/save-task"

def call_endpoint_save(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    response = requests.post(url = API_ENDPOINT, json=body_json)
