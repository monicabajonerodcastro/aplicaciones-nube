import zipfile, os
from constants import BUCKET_NAME_GCP
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcloud.json"
storage_client = storage.Client()

def my_compress_file_GCP(file_name, new_format):
    
    split_file_name = file_name.split(".")
    if (len(split_file_name) > 1) :
        file_name_no_extension = split_file_name[0]
    else:
        file_name_no_extension = file_name

    bucket = storage_client.get_bucket(BUCKET_NAME_GCP)
    blob = bucket.get_blob(file_name)
    object_bytes = blob.download_as_string()
    new_file_name_no_ext = file_name_no_extension.split("/")[1]
    new_file_name = new_file_name_no_ext + "." + new_format
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