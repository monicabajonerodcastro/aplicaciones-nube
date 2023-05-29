import json, base64
from constants import BUCKET_NAME_GCP, UPLOAD_FOLDER

import os
from google.cloud import storage, pubsub_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcloud.json'

storage_client = storage.Client()
publisher = pubsub_v1.PublisherClient()

def remove_extension_from_file(file_name):
    split_name = file_name.split(".")
    split_name.pop(len(split_name)-1)
    name_no_ext = ".".join(split_name)
    return name_no_ext    

def build_extension_from_file(file_name):
    split_name = file_name.split(".")
    ext = split_name.pop(len(split_name)-1)
    return ext

def publish_message_gcp(topic_name, message):
    message_to_publish = json.dumps(message).encode('utf-8')
    future = publisher.publish(topic_name, message_to_publish)
    future.result()

def build_file_name(blob_name, bucket_name):
    file_name_no_ext = remove_extension_from_file(blob_name)
    extension = build_extension_from_file(blob_name)
    blobs = storage_client.list_blobs(bucket_name)
    cont = 0
    for blob in blobs:
        file_name = blob.name
        if file_name.startswith(UPLOAD_FOLDER):
            split_name = file_name.split("/")
            if len(split_name) > 1 and len(split_name[1]) > 0:
                bucket_file_no_ext = remove_extension_from_file(split_name[1])
                if(file_name_no_ext == bucket_file_no_ext):
                    cont = cont + 1
                elif bucket_file_no_ext.startswith(file_name_no_ext+"("):
                    cont = cont + 1
    if cont > 0:
        return file_name_no_ext + "({})".format(cont) + "." + extension
    return file_name_no_ext + "." + extension
                

def send_to_bucket(blob_name, file, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    new_file_name = build_file_name(blob_name, bucket_name)
    blob = bucket.blob(UPLOAD_FOLDER + new_file_name)
    blob.upload_from_file(file)
    return new_file_name

def download_file_from_bucket(file_name):
    bucket = storage_client.get_bucket(BUCKET_NAME_GCP)
    blob = bucket.get_blob(file_name)
    data = blob.download_as_string()
    return base64.b64encode(data)