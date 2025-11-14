import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__ == "__main__":
    # create 2 process
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    # start the timer
    start = time.time()

    # start the process
    p1.start()
    p2.start()

    # joining the process to the main thread
    p1.join()
    p2.join()

    finished_time = time.time()-start

    print(finished_time)