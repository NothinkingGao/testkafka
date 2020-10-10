#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2020-09-24 15:56:04
# Description:kafka消费者消息测试
from kafka import KafkaConsumer

consumer = KafkaConsumer("mytopic4",group_id = 'group1')
for msg in consumer:
    print(msg)



