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

```bash
$ python producer.py
```

## Running the consumers

You can run one or both of the consumers.  The producer publishes to 4 partitions, these will be automatically 
distributed across the partitions.  When both consumers are running they each consumer 2 partitions. 
Stopping or starting a consumer will cause the partitions to rebalance to the other consumer.

```bash
$ python consumer.py
```
