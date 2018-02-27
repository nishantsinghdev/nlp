from kafka import KafkaConsumer
# To consume messages
consumer = KafkaConsumer('my-topic',
group_id='my_group',
bootstrap_servers=['localhost:9092'])
for message in consumer:
# message value is raw byte string -- decode if necessary!
# e.g., for unicode: `message.value.decode('utf-8')`
	print("%s" % (message.value))
