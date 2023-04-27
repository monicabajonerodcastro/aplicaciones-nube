## VARIABLES CLOUD

HOST_RABBIT_MQ = '35.219.174.216'
API_ENDPOINT_PUBLISH = "http://34.125.239.40:5002/publish-pending-tasks" 
API_ENDPOINT_SAVE = "http://34.125.239.40:5002/save-task"
API_ENDPOINT_PROCESS = "http://34.125.239.40:5002/process-task/{}"   
UPLOAD_FOLDER = "/mnt/nfs_clientshare" 
UPLOAD_PROCESSED_FOLDER = "/mnt/nfs_clientshare/{}.{}"
HOST_POSTGRES = '34.125.79.66'
USER_POSTGRES = "test_user"
PASSWORD_POSTGRES = "postgres"
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