# Docker Kafka Python

## Overview
Example of running Kafka in Docker, and a producer and consumer in Python.

## Implementation
When the Kafka container is running, run producer.py.  It will publish messages to Kafka.  Run consumer.py.  It will consume the messages.

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

## Running the consumer

```bash
$ python consumer.py
```
