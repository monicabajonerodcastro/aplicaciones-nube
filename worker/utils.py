#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
print(os.path.join("/".join(os_path)))
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import zipfile
from constants import UPLOAD_PROCESSED_FOLDER
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'archivos-384418-746a4b2b24fa.json'
storage_client = storage.Client()

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

def my_compress_file_GCP(bucket_name, file_name, new_format):
    split_file_name = file_name.split(".")
    if (len(split_file_name) > 1) :
        file_name_no_extension = split_file_name[0]
    else:
        file_name_no_extension = file_name

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(file_name)
    object_bytes = blob.download_as_string()
    new_file_name = file_name_no_extension + "." + new_format
    myZip = zipfile.ZipFile(new_file_name, 'w')
    myZip.writestr(file_name, object_bytes, compress_type=zipfile.ZIP_DEFLATED)
    myZip.close()
    send_to_bucket(new_file_name, new_file_name, 'poc-bucket-python')
    os.remove(new_file_name)
    return new_file_name

def send_to_bucket(blob_name, file_name, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)
    return blob