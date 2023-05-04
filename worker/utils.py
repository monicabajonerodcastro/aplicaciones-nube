#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
print(os.path.join("/".join(os_path)))
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import zipfile
from constants import UPLOAD_PROCESSED_FOLDER

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