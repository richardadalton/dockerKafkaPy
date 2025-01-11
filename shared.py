from kafka import KafkaConsumer
import json

BROKER = 'localhost:29092'
TOPIC = 'testnum'
GROUP_ID = 'basic_consumer'

def get_consumer():
    return KafkaConsumer(
        bootstrap_servers=BROKER,
        value_deserializer=lambda v: json.loads(v.decode('ascii')),
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        group_id=GROUP_ID,
    )

def listen(consumer):
    consumer.subscribe(topics=[TOPIC], )
    for message in consumer:
        print("%d:%d: v=%s" % (message.partition,
                               message.offset,
                               message.value))
        consumer.commit()
