from random import random
import asyncio

async def fry_rice():
    value = 1 + random()
    print("Cooking frying rice ",{value},'sec')
    await asyncio.sleep(value)
    return f"\n \t Fry rice Finished {value}  sec"
    
async def noodle():
    value = 1 + random()
    print("Cooking noodle",{value},'sec')
    await asyncio.sleep(value)
    return f"\n \t Noodle Finished {value} sec "
    
async def curry():
    value = 1 + random()
    print("Cooking curry",{value},'sec')
    await asyncio.sleep(value)
    return f"\n \t Curry Finished {value} sec "
    
# main
async def main():
    fry_rice_task = asyncio.create_task(fry_rice(), name = 'rice')
    noodle_task = asyncio.create_task(noodle(), name = 'noodle')
    curry_task = asyncio.create_task(curry(), name= 'curry')
    menu = [fry_rice_task, noodle_task, curry_task]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(menu, return_when=asyncio.FIRST_COMPLETED)
    # report results
    # print('Done')
    # get the first task to complete
    first = done.pop()
    print(first.result()) 
    # print(first.get_name())
    
    print(f'\n Uncomplete, {len(pending)} task uncomplete')
    
#start the asyncio program
asyncio.run(main())