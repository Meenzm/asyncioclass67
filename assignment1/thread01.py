# running a function in another thread
from time import sleep, ctime
from threading import Thread

# a custom function that block for a moe=ment
def task():
    #block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')
    
# crate a thread
thread = Thread(target=task)
#run the thrad
thread.start()
#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()