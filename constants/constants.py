"""
## VARIABLES DOCKER-LOCAL
HOST_RABBIT_MQ = '192.168.1.8'

API_ENDPOINT_PUBLISH = "http://192.168.1.8:5002/publish-pending-tasks" 
API_ENDPOINT_SAVE = "http://192.168.1.8:5002/save-task"

API_ENDPOINT_PROCESS = "http://192.168.1.8:5004/process-task/{}"   

UPLOAD_FOLDER = "/mnt/nfs_clientshare" 
UPLOAD_PROCESSED_FOLDER = "/mnt/nfs_clientshare/{}.{}"
HOST_POSTGRES = '192.168.1.8'
USER_POSTGRES = "postgres"
PASSWORD_POSTGRES = "postgres"
"""

## VARIABLES CLOUD
HOST_RABBIT_MQ = '34.125.164.151'

API_ENDPOINT_PUBLISH = "http://34.16.148.106:5002/publish-pending-tasks" 
API_ENDPOINT_SAVE = "http://34.16.148.106:5002/save-task"

API_ENDPOINT_PROCESS = "http://34.125.200.65:5004/process-task/{}"   
UPLOAD_FOLDER = "/mnt/nfs_clientshare" 

UPLOAD_PROCESSED_FOLDER = "/mnt/nfs_clientshare/{}.{}"
HOST_POSTGRES = '34.68.54.144'
USER_POSTGRES = "postgres"
PASSWORD_POSTGRES = "test_user"

"""
## VARIABLES LOCAL
HOST_RABBIT_MQ = 'localhost'
API_ENDPOINT_PUBLISH = "http://127.0.0.1:5000/publish-pending-tasks"
API_ENDPOINT_SAVE = "http://127.0.0.1:5000/save-task"
API_ENDPOINT_PROCESS = "http://127.0.0.1:5000/process-task/{}" 
UPLOAD_FOLDER = "/Users/mbajonero/Downloads/uploaded-files" 
UPLOAD_PROCESSED_FOLDER = "/Users/mbajonero/Downloads/processed-files/{}.{}"
HOST_POSTGRES = '127.0.0.1'
USER_POSTGRES = "postgres"
PASSWORD_POSTGRES = "postgres"
"""