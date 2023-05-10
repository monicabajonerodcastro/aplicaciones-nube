#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import requests, json
from constants import API_ENDPOINT_SAVE, API_ENDPOINT_PROCESS

def call_endpoint_save(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    r = requests.post(url = API_ENDPOINT_SAVE, json=body_json)
    #r = requests.post(url="http://localhost:5010/save-task", json=body_json)
    return r

def call_endpoint_process(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    r = requests.post(url = API_ENDPOINT_PROCESS.format(body_json["id"])) 
    #r = requests.post(url="http://localhost:5003/process-task/" + body_json["id"], json=body_json)
    return r 