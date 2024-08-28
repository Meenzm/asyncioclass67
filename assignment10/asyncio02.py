# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    start_time_pc = time.perf_counter()
    # start time
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_time_pc = time.perf_counter() - start_time_pc
    print('Producer: Done')
    print(f"Produce  time: {end_time_pc} seconds")

    

 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    start_time_cm = time.perf_counter()
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    end_time_cm = time.perf_counter() - start_time_cm
    # all done
    print('Consumer: Done')
    print(f"Consumer  time: {end_time_cm} sec")

 
# entry point coroutine
async def main():
    start_time = time.perf_counter()
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.perf_counter() - start_time 
    print(f'Overall time: {end_time} sec')
 
# start the asyncio program
asyncio.run(main())