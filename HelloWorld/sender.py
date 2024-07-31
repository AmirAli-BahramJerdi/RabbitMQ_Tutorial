import pika
# sender as publisher
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


'''
At this point we're ready to send a message. Our first message will just 
contain a string "Hello World!" and we want to send it to our hello queue.
'''
channel.basic_publish(
    exchange='',
    routing_key='hello', # the name must be the same as queue 
    body='Hello World!'
)
print(" [x] Sent 'Hello World!'")


'''
Before exiting the program we need to make sure the network buffers 
were flushed and our message was actually delivered to RabbitMQ. 
We can do it by gently closing the connection.
'''
connection.close()