#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
print(os.path.join("/".join(os_path)))
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import zipfile
from constants import BUCKET_NAME_GCP, RUTA_JSON_GCP
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = RUTA_JSON_GCP
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcloud.json"
storage_client = storage.Client()

def my_compress_file_GCP(file_name, new_format):
    file_name_no_folder = file_name.split("/")[1]

    split_file_name = file_name_no_folder.split(".")
    if (len(split_file_name) > 1) :
        file_name_no_extension = split_file_name[0]
    else:
        file_name_no_extension = file_name_no_folder

    bucket = storage_client.get_bucket(BUCKET_NAME_GCP)
    blob = bucket.get_blob(file_name)
    object_bytes = blob.download_as_string()
    new_file_name = file_name_no_extension + "." + new_format
    myZip = zipfile.ZipFile(new_file_name, 'w')
    myZip.writestr(file_name, object_bytes, compress_type=zipfile.ZIP_DEFLATED)
    myZip.close()
    send_to_bucket(new_file_name, new_file_name, BUCKET_NAME_GCP)
    os.remove(new_file_name)
    return new_file_name

def send_to_bucket(blob_name, file_name, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)
    return blob