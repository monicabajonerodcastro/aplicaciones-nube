## VARIABLES DOCKER

HOST_RABBIT_MQ = 'rabbitmq'
API_ENDPOINT_PUBLISH = "http://microservice-api:5002/publish-pending-tasks" 
API_ENDPOINT_SAVE = "http://microservice-api:5002/save-task"
API_ENDPOINT_PROCESS = "http://microservice-api:5002/process-task/{}"   
UPLOAD_FOLDER = "/microservice-api/uploaded-files" 
UPLOAD_PROCESSED_FOLDER = "/microservice-api/processed-files/{}.zip"
"""

## VARIABLES LOCAL
HOST_RABBIT_MQ = 'localhost'
API_ENDPOINT_PUBLISH = "http://127.0.0.1:5000/publish-pending-tasks"
API_ENDPOINT_SAVE = "http://127.0.0.1:5000/save-task"
API_ENDPOINT_PROCESS = "http://127.0.0.1:5000/process-task/{}" 
UPLOAD_FOLDER = "/Users/mbajonero/Downloads/uploaded-files" 
UPLOAD_PROCESSED_FOLDER = "/Users/mbajonero/Downloads/processed-files/{}.zip"
"""