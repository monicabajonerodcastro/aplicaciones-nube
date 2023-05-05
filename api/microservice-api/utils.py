#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import pika, json
from constants import HOST_RABBIT_MQ

import os
from google.cloud import storage

#TODO -> el valor es la ubicacion del archivo llave para acceder al bucket, debe cambiarse por la ruta de la
#TODO -> llave y agregar ese archivo llave tipo JSON al docker
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'archivos-384418-746a4b2b24fa.json'
storage_client = storage.Client()

def publish_message(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBIT_MQ))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=json.dumps(message))
    print(" ======================= Message sent to the queue {} =======================".format(queue), flush=True)
    connection.close()

def compress_local_file(path, new_format):
    split_path = path.split("/")
    file_name = split_path[len(split_path)-1]
    split_file_name = file_name.split(".")
    if (len(split_file_name) > 1) :
        file_name_no_extension = split_file_name[0]
    else:
        file_name_no_extension = file_name

    my_zip = zipfile.ZipFile(UPLOAD_PROCESSED_FOLDER.format(file_name_no_extension, new_format), 'w')
    my_zip.write(path, compress_type=zipfile.ZIP_DEFLATED)
    my_zip.close()
    return UPLOAD_PROCESSED_FOLDER.format(file_name_no_extension, new_format)

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

def get_file_path_GCP(url, file_path):
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(url, f)

def my_compress_file_GCP(bucket_name, file_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(file_name)
    object_bytes = blob.download_as_string()
    myZip = zipfile.ZipFile('myZip.zip', 'w')
    myZip.writestr(file_name, object_bytes, compress_type=zipfile.ZIP_DEFLATED)
    myZip.close()