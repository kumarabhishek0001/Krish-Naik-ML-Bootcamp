import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1) #This simulates Io/file-reading/networking operation
        return f"Number: {i}"

def print_letters():
    for i in 'abcde':
        time.sleep(1) #This simulates Io/file-reading/networking operation
        print(f"Letters: {i}")

# creating 2 thread to handle each function
t1 = threading.Thread(target=print_letters)
t2 = threading.Thread(target=print_numbers)


# starting the recording time
start = time.time()

# threads start working
t1.start()
t2.start()

# waiting for thread to completed working and join them to the main thread
t1.join()
t2.join()

time_taken = time.time()-start
print("time taken for execution: ",time_taken)