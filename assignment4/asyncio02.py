# example of starting many tasks and getting access to all tasks
import asyncio

# coroutine for a task
async def task_coroutine(value):
    #report a message
    print(f"task {value} is runing")
    #block for a moment
    await asyncio.sleep(1)
    
# define a main corutine
async def main():
    # report a message
    print('main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i) for i in range(10))]
    #allow some of tasks time to start
    await asyncio.sleep(0.1)
    # get all task
    tasks = asyncio.all_tasks()
    # report all tasks
    for task in tasks:
        print(f'>{task.get_name()}, {task.get_coro()}')
    # wait for all tasks to conplete
    for task in started_tasks:
        await task
        
# start the asycio program
asyncio.run(main())