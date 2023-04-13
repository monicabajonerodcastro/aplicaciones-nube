#Import constants
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'constants'))

import requests, json
from constants import API_ENDPOINT_SAVE, API_ENDPOINT_PROCESS

def call_endpoint_save(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    requests.post(url = API_ENDPOINT_SAVE, json=body_json)

def call_endpoint_process(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    requests.post(url = API_ENDPOINT_PROCESS.format(body_json["id"])) 