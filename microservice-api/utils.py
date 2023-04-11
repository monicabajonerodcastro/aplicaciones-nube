import pika, json, zipfile

HOST_RABBIT_MQ = 'rabbitmq'
#HOST_RABBIT_MQ = 'localhost' -> Comentar para Docker. Quitar comentario para local

#UPLOAD_PROCESSED_FOLDER = "/Users/mbajonero/Downloads/processed-files/{}.zip" -> Comentar para Docker. Quitar comentario para local
UPLOAD_PROCESSED_FOLDER = "/microservice-api/processed-files/{}.zip"

def publish_message(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBIT_MQ))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=json.dumps(message))
    print(" ======================= Message sent to the queue {} =======================".format(queue), flush=True)
    connection.close()

def compress_local_file(path):
    split_path = path.split("/")
    file_name = split_path[len(split_path)-1]
    split_file_name = file_name.split(".")
    if (len(split_file_name) > 1) :
        file_name_no_extension = split_file_name[0]
    else:
        file_name_no_extension = file_name

    my_zip = zipfile.ZipFile(UPLOAD_PROCESSED_FOLDER.format(file_name_no_extension), 'w')
    my_zip.write(path, compress_type=zipfile.ZIP_DEFLATED)
    my_zip.close()
    return UPLOAD_PROCESSED_FOLDER.format(file_name_no_extension)