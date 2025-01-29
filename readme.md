# Docker Kafka Python

## Overview
Example of running Kafka in Docker, and a producer and consumer in Python.

## Implementation
When the Kafka container is running, run producer.py.  It will publish messages to Kafka.  
Running one or both of consumer1.py and consumer2.py will consume the messages.

## Installation

Just clone this repository

```bash
$ git clone https://github.com/richardadalton/dockerKafkaPy
```

Create the virtual environment, and install dependencies.

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```

Run the Docker containers.

```bash
$ docker-compose up
```

## Running the producer

The first time you run the producer it will create the 'testnum' topic that the consumers will connect to.
It will use one partition by default.  If you run more than one consumer with only one partition, then only
one consumer will receive messages.

```bash
$ python producer.py
```

## Create Additional Partitions (optional)

If you run the admin.py script, you will create three additional partitions.  Now running multiple consumers will
cause the partitions to be allocated to the multiple paritions.

```bash
$ python admin.py
```

## Running the consumers

You can run one or both of the consumers.  The producer publishes to 4 partitions, these will be automatically 
distributed across the partitions.  When both consumers are running they each consume 2 partitions. 
Stopping or starting a consumer will cause the partitions to rebalance to the other consumer.

Both consumers in this example use the same group, so a message from the producer will be processed by one or the 
other consumer, but not both.

```bash
$ python consumer1.py
$ python consumer2.py
```
