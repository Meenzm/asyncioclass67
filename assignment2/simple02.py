# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes
from time import sleep, ctime, time

# cooking synchronose
def cooking(index):
    print(f"{ctime()} Kitchen-{index}   : Begin cook...")
    sleep(2)
    print(f'{ctime()} Kitchen-{index}   : Cooking done!')

if __name__ == '__main__':
    # Begin of main thread
    print(f'{ctime()} Main   : Start cooking.')
    start_time = time()
    # Cooking for each dish
    for index in range(2):
        cooking(index)
    
    duration = time() - start_time
    print(f'{ctime()} Main   : Finished Cooking duration in {duration:02f} seconds.')   