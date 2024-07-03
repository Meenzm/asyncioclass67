# example of getting the current task from the main coroutine
import asyncio

# define a main coroutine
async def main():
    #report a message
    print("main coroutine starting")
    # get the current task
    task = asyncio.current_task()
    # report its detail
    print(task)
    
# start the asycio program
asyncio.run(main())