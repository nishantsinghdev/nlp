from speech2txt import trial
from kafka import SimpleProducer, KafkaClient
# To send messages synchronously
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
speech_to_text=trial()

# Note that the application is responsible for encoding messages to type bytes
producer.send_messages(b'my-topic',bytes(speech_to_text))
