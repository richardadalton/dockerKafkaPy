from kafka import KafkaAdminClient
from kafka.admin.new_partitions import NewPartitions
from shared import BROKER, TOPIC

def configure_kafka(partitions):
    client = KafkaAdminClient(bootstrap_servers=[BROKER])

    rsp = client.create_partitions({
        TOPIC: NewPartitions(partitions)
    })
    print(rsp)

def main():
    configure_kafka(4)

if __name__ == "__main__":
    main()