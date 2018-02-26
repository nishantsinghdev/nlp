
# coding: utf-8

# In[ ]:


from kafka import KafkaClient, SimpleProducer, SimpleConsumer
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
topic = 'test'
msg = b'Hello World'
producer.send_messages(topic, msg)
producer.send_messages(topic, msg, b'Hey again!', b'See ya')
producer = SimpleProducer(kafka, async=True)
#producer = SimpleProducer(kafka, req_acks = SimpleProducer.ACK_AFTER_LOCAL_WRITE)
consumer = SimpleConsumer(kafka, 'python','test')
for msg in consumer:
    print(msg)


# In[16]:


from kafka import SimpleProducer, KafkaClient 

def print_response(response=None):
    if response:
        print('Error: {0}'.format(response[0].error))
        print('Offset: {0}'.format(response[0].offset))


def main():
    kafka = KafkaClient('localhost:9092')
    producer = SimpleProducer(kafka)

    topic = 'test'
    msg = b'Hello World'

    print_response(producer.send_messages(topic, msg))

    kafka.close()

if __name__ == "__main__":
    main()

