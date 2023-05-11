#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import json 

from google.cloud import pubsub_v1
from concurrent import futures

from service import call_endpoint_save
from constants import PROJECT_NAME, SUBSCRIPTION_REQUEST_NAME

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_NAME, SUBSCRIPTION_REQUEST_NAME)

def callback(message):
    print(" ======================= Request Received =======================", flush=True)
    response = call_endpoint_save(message.data)
    print(response.content)
    if(response.status_code == 200):
        message.ack()

future = subscriber.subscribe(subscription_path, callback=callback)

with subscriber:
    try:
        future.result()
    except futures.TimeoutError:
        future.cancel()  
        future.result()  
