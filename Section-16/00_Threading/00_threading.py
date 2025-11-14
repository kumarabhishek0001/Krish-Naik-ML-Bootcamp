# without multithreading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1) #This simulates Io/file-reading/networking operation
        print(f"Number: {i}")

def print_letters():
    for i in 'abcde':
        time.sleep(1) #This simulates Io/file-reading/networking operation
        print(f"Letters: {i}")

# starting the recording time
start = time.time()

# calling the function
print_numbers()
print_letters()

time_taken = time.time()-start
print("time taken for execution: ",time_taken)