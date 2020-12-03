#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2020-09-24 15:56:04
# Description:kafka消费者消息测试
from kafka import KafkaConsumer
from kafka.structs import TopicPartition,OffsetAndMetadata
import time
poll_time = 300
consumer = KafkaConsumer("testtopic",group_id = 'mygroup',enable_auto_commit=False)

while True:
    print("poll message from kafka...")
    record = consumer.poll(poll_time)
    #print(record)

    for records in record.values():
        for msg in records:
            print(msg)
            consumer.commit({
                TopicPartition(msg.topic,msg.partition):OffsetAndMetadata(msg.offset + 1,"")
            })
            time.sleep(5)
            
    
    consumer.commit()



