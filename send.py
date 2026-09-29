import pika 
import json 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 

channel = connection.channel()

channel.queue_declare(queue='user_status')

message_data = {'user':'Jake','complaince':True}

channel.basic_publish(exchange='',routing_key='user_status',body=json.dumps(message_data))

print('sent message ')

connection.close()