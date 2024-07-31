import pika
# reciever as consumers
connection = pika.BlockingConnection(
    # ConnectionParameters for rabbitmq 
    parameters=pika.ConnectionParameters(host='localhost')
)
channel = connection.channel() # for managing connections that connected to rabbitmq
'''
We're connected now, to a broker on the local machine - hence the localhost. 
If we wanted to connect to a broker on a different machine we'd simply specify 
its name or IP address here.
'''


channel.queue_declare(queue='hello') # making queue for message broker named 'hello'
'''
A Channel is the primary communication method for interacting with RabbitMQ. 
It is recommended that you do not directly invoke the creation of a channel 
object in your application code but rather construct a channel by calling 
the active connections channel() method.
'''


def call_back(channel, method, properties, body):
    print(f'Received {body}')


channel.basic_consume(
    queue='hello',
    on_message_callback=call_back,
    auto_ack=True, #message that consumer sent to broker, for deleting the message
)
'''
Sends the AMQP 0-9-1 command Basic.Consume to the broker and binds messages for the consumer_tag 
to the consumer callback. If you do not pass in a consumer_tag, one will be automatically generated for you. 
Returns the consumer tag.
'''


print("Waiting for message, to exit use ctrl+C")

channel.start_consuming()
'''Processes I/O events and dispatches timers and basic_consume callbacks until all consumers are cancelled.'''