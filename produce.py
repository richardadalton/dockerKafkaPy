from time import sleep
from json import dumps

from kafka import KafkaProducer
import random
from shared import BROKER, TOPIC

firstnames = ['John', 'George', 'Paul', 'Ringo',
              'Tom', 'Dick', 'Harry',
              'Mary', 'Nora', 'Cheryl', 'Tina']

lastnames = ['Lennon', 'Harrison', 'McCartney', 'Starr',
             'Wolf', 'Nixon', 'Houdini',
             'Lincoln', 'Gaule', 'Callaghan', 'Turner']

def get_producer():
    # initializing the Kafka producer
    return KafkaProducer (
        bootstrap_servers=[BROKER],
        value_serializer=lambda x:dumps(x).encode('ascii'),
    )

def send_data(producer):
    # generating the numbers ranging from 1 to 500
    for n in range(500):
        fn = random.choice(firstnames)
        ln = random.choice(lastnames)
        fullname = '{0} {1}'.format(fn, ln)
        my_data = {'num': n, 'fullname': fullname}
        producer.send('testnum', value = my_data)
        sleep(1)

    producer.flush()

def main():
    producer = get_producer()
    send_data(producer)

if __name__ == "__main__":
    main()