#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2020-09-24 15:30:45
# Description: kafka生产者测试
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from kafka import KafkaProducer

messagese = {
   "test": "message1",
   "test2": "messge2",
   "test3": "message3"
}

total = 2

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

def run(start,end):
    for item in range(int(start),int(end)):
        key = "{}key_mykey".format(item)
        producer.send('testtopic',b"message")
    return True

def run_single():
    '''
       单线程
    '''
    for i in range(10):
        result =producer.send('testtopic',b"message,ojbk,ojbk...")
        print(result)
    time.sleep(10)
    #run(0,total)

def multiy_threads():
    '''
        多线程
    '''
    step = int(total / 10)
    trs = [ threading.Thread(target = run,args = (i*step,(i+1)*step)) for i in range(10) ]

    for item in trs:
        item.start()
        item.join()

def thread_pool():
    '''
        线程池
    '''
    executor = ThreadPoolExecutor(max_workers = 10)
    futures = list()
    step = int(total / 10)
    for i in range(10):
        future = executor.submit(run,i*step,(i+1)*step)
        futures.append(future)

    executor.shutdown(True)

    for item in futures:
        print(item.result())

def multiply_process():
    step = int(total / 10)
    progresses = [multiprocessing.Process(target = run,args = (i*step,(i+1)*step)) for i in range(10)]
    
    for item in progresses:
        item.start()

def process_pool():
    '''进程池'''
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    step = int(total / 10)
    results = list()
    for i in range(10):
        result = pool.apply_async(run,args = (i*step,(i+1)*step ))
        results.append(result)

    for item in results:
        item.get()

def spy_code():
    '''
     事件管理的伪代码
    '''
    pass


#producer.close()
#print("发送数据结束---")

if __name__ == '__main__':
    #thread_pool() # 2.666s
    run_single() # 8.01s
    #multiy_threads() # 19.227s
    #multiply_process() # 2.594s
    #process_pool() # 3.086s





