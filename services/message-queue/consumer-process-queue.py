#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

from google.cloud import pubsub_v1
from concurrent import futures

import sys, os
from service import call_endpoint_process
from constants import PROJECT_NAME, SUBSCRIPTION_PROCESS_NAME

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_NAME, SUBSCRIPTION_PROCESS_NAME)

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

 