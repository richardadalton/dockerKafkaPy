from time import sleep
from json import dumps
from kafka import KafkaProducer
import random


firstnames = ['John', 'George', 'Paul', 'Ringo',
              'Tom', 'Dick', 'Harry',
              'Mary', 'Nora', 'Cheryl', 'Tina']

lastnames = ['Lennon', 'Harrison', 'McCartney', 'Starr',
             'Wolf', 'Nixon', 'Houdini',
             'Lincoln', 'Gaule', 'Callaghan', 'Turner']

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda x:dumps(x).encode('ascii')
)

# generating the numbers ranging from 1 to 500
for n in range(500):
    fn = random.choice(firstnames)
    ln = random.choice(lastnames)
    fullname = '{0} {1}'.format(fn, ln)
    my_data = {'num': n, 'fullname': fullname}
    my_producer.send('testnum', value = my_data)
    sleep(1)

