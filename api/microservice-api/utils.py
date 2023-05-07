#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import pika, json, base64
from constants import HOST_RABBIT_MQ, RUTA_JSON_GCP, BUCKET_NAME_GCP

import os
from google.cloud import storage

#TODO -> el valor es la ubicacion del archivo llave para acceder al bucket, debe cambiarse por la ruta de la
#TODO -> llave y agregar ese archivo llave tipo JSON al docker
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcloud.json'
storage_client = ##storage.Client()

def publish_message(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBIT_MQ))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=json.dumps(message))
    print(" ======================= Message sent to the queue {} =======================".format(queue), flush=True)
    connection.close()

def test_connect_ucket(bucket_name):
    my_bucket = storage_client.get_bucket(bucket_name)
    print(vars(my_bucket))

def send_to_bucket(blob_name, file, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_file(file)
    return blob

def get_file_from_bucket(blob_name, file_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(blob, f)
        return base64.b64encode(f.read())

def get_file_path_GCP(url, file_path):
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(url, f)

def download_file_from_bucket(file_name):
    bucket = storage_client.get_bucket(BUCKET_NAME_GCP)
    blob = bucket.get_blob(file_name)
    data = blob.download_as_string()
    return base64.b64encode(data)