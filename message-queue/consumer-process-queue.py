import pika, sys, os
from service import call_endpoint_process

HOST_RABBIT_MQ = 'rabbitmq'
#HOST_RABBIT_MQ = 'localhost' -> Comentar para Docker. Quitar comentario para local

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBIT_MQ))
    channel = connection.channel()
    channel.queue_declare(queue="processes_queue")

    def callback(ch, method, properties, body):
        print(" ======================= Process Received =======================", flush=True)
        call_endpoint_process(body)

    channel.basic_consume(queue="processes_queue", auto_ack=True, on_message_callback=callback)
    print(" *********************** Waiting for incoming processes ***********************", flush=True)

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
