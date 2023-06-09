#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

from google.cloud import pubsub_v1
from concurrent import futures

import sys, os, json, requests
from constants import PROJECT_NAME, SUBSCRIPTION_PROCESS_NAME, API_ENDPOINT_PROCESS, RUTA_JSON_GCP

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = RUTA_JSON_GCP
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcloud.json'

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_NAME, SUBSCRIPTION_PROCESS_NAME)

def call_endpoint_process(body):
    body_decoded = body.decode("utf-8")
    body_json = json.loads(body_decoded)
    r = requests.post(url = API_ENDPOINT_PROCESS.format(body_json["id"])) 
    #r = requests.post(url="http://localhost:5003/process-task/" + body_json["id"], json=body_json)
    return r 

def callback(message):
    print(" ======================= Process Received =======================", flush=True)
    response = call_endpoint_process(message.data)
    print(response.content)
    if(response.status_code == 200):
        message.ack()

future = subscriber.subscribe(subscription_path, callback=callback)

with subscriber:
    try:
        future.result()
    except futures.TimeoutError:
        future.cancel()  # Trigger the shutdown.
        future.result()  # Block until the shutdown is complete.

 