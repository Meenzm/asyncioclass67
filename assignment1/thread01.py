#ส่งการบ้าน01
# running a function in another thread
from time import sleep, ctime
from threading import Thread

<<<<<<< HEAD
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
=======
# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
>>>>>>> 3970926c92ff939fa8cee033ec5ab6e687e5eeab
print(f'{ctime()} Waiting for the thread...')
thread.join()