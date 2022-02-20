from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda v: json.loads(v.decode('ascii')),
    auto_offset_reset='earliest'
)

consumer.subscribe(topics='testnum')
for message in consumer:
    print ("%d:%d: v=%s" % (message.partition,
                            message.offset,
                            message.value))

