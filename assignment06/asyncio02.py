# example of an asynchronous iterator with async for loop
import asyncio

# define an asynchronous iterator
class AsynIterator:
    #contructor, define some state
    def __init__(self):
        self.counter = 0
    
    # creat an instance if the iterator
    def __aiter__(self):
        return self
    
    # return the next awitable
    async def __anext__(self):
        # check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter
    
# main coroutine
async def main():
    # loop over async iterator with async for loop
    async for item in AsynIterator():
        print(item)

# execute the asyncio program
asyncio.run(main())