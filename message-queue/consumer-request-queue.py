import pika, sys, os

HOST_RABBIT_MQ = 'rabbitmq'

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBIT_MQ))
    channel = connection.channel()
    channel.queue_declare(queue="requests_queue")

    def callback(ch, method, properties, body):
        print(" ======================= Request Received =======================", flush=True)
        #TODO

    channel.basic_consume(queue="requests_queue", auto_ack=True, on_message_callback=callback)
    print(" *********************** Waiting for incoming requests ***********************", flush=True)

    channel.start_consuming()

print(__name__)
if __name__ == '__main__':
    try:
        main()
    except:
        print(" *********************** Process interrupted ***********************", flush=True)
        try:
            sys.exit(0)
        except:
            os.exit(0)
