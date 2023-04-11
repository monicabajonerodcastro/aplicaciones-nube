import pika, sys, os
from service import call_endpoint_save

#HOST_RABBIT_MQ = 'rabbitmq'
HOST_RABBIT_MQ = 'localhost'

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
        print(e)
        try:
            sys.exit(0)
        except:
            os._exit(0)
