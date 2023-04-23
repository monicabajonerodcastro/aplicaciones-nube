## VARIABLES CLOUD

HOST_RABBIT_MQ = '35.219.174.216'
API_ENDPOINT_PUBLISH = "http://host.docker.internal:5008/publish-pending-tasks" 
API_ENDPOINT_SAVE = "http://host.docker.internal:5008/save-task"
API_ENDPOINT_PROCESS = "http://host.docker.internal:5008/process-task/{}"   
UPLOAD_FOLDER = "/api/microservice-api/uploaded-files" 
UPLOAD_PROCESSED_FOLDER = "/api/microservice-api/processed-files/{}.{}"
HOST_POSTGRES = '34.125.22.159'
"""

## VARIABLES LOCAL
HOST_RABBIT_MQ = 'localhost'
API_ENDPOINT_PUBLISH = "http://127.0.0.1:5000/publish-pending-tasks"
API_ENDPOINT_SAVE = "http://127.0.0.1:5000/save-task"
API_ENDPOINT_PROCESS = "http://127.0.0.1:5000/process-task/{}" 
UPLOAD_FOLDER = "/Users/mbajonero/Downloads/uploaded-files" 
UPLOAD_PROCESSED_FOLDER = "/Users/mbajonero/Downloads/processed-files/{}.{}"
HOST_POSTGRES = '127.0.0.1'
"""