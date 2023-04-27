#Import constants
import sys, os
os_path = os.path.dirname(sys.path[0]).split("/")
del os_path[len(os_path) - 1]
if len(os_path) > 1 : sys.path.append(os.path.join("/".join(os_path),'constants'))
else: sys.path.append(os.path.join("/",'constants'))

import pika
from service import call_endpoint_save
from constants import HOST_RABBIT_MQ

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBIT_MQ))
    channel = connection.channel()
    channel.queue_declare(queue="requests_queue")

    def callback(ch, method, properties, body):
        print(" ======================= Request Received =======================", flush=True)
        call_endpoint_save(body)

    channel.basic_consume(queue="requests_queue", auto_ack=True, on_message_callback=callback)
    print(" *********************** Waiting for incoming requests ***********************", flush=True)

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(" *********************** Process interrupted ***********************", flush=True)
        print(e, flush=True)
        try:
            sys.exit(0)
        except:
            os._exit(0)
 