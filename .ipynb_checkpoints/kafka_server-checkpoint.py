import producer_server


def run_kafka_server():
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="crime.statistics",
        bootstrap_servers="localhost:9092",
        client_id="SF Crime Statistics"
    )
    print(producer)
    return producer


def feed():
    producer = run_kafka_server()
    print(producer)
    #producer.send('sample', b'Hello, World!')
    producer.send('crime.sample', key=b'message-two', value=b'This is Kafka-Python')
    producer.generate_data()


if __name__ == "__main__":
    feed()
