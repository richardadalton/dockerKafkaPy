from shared import get_consumer, listen


def main():
    consumer = get_consumer()
    listen(consumer)


if __name__ == "__main__":
    main()
