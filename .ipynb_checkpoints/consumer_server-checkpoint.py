from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('crime.statistics', 
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    print (json.loads(message.value.decode('utf-8')))