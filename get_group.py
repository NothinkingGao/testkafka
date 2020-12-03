#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2020-11-30 17:50:24
# Description:some description


from kafka import BrokerConnection
from kafka.protocol.admin import *
import socket

bc = BrokerConnection('localhost', 9092, socket.AF_INET)
bc.connect_blocking()

list_groups_request = ListGroupsRequest_v1()

future = bc.send(list_groups_request)
while not future.is_done:
    for resp, f in bc.recv():
        f.success(resp)

for group in future.value.groups:
    print(group)
