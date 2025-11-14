import multiprocessing
import math
import sys
import time
# increasing the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of given number
def compute_factorial(number):
    print(f"factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of number is {result}")
    return result

if __name__ == "__main__":

    number_list = [5000,6000,7000,8000]

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(compute_factorial,number_list)

    end_time = time.time()-start_time

    print(f"result = {result}")
    print(f"Time taken: {end_time}s")