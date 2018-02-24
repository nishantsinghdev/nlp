
# coding: utf-8

# In[2]:


from audio2texting import t
from kafka import KafkaClient, SimpleProducer, SimpleConsumer
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

a = 'brian.wav'

topic = 'test'
msg=t(a)
msg


# In[3]:


producer.send_messages(topic, bytes(msg,encoding='utf-8'))
producer = SimpleProducer(kafka, async=True)
producer = SimpleProducer(kafka, req_acks = SimpleProducer.ACK_AFTER_LOCAL_WRITE)


# In[ ]:


consumer = SimpleConsumer(kafka, 'python','test')
for msg in consumer:
    print(msg)


# In[ ]:


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

