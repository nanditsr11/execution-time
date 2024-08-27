# Calculate time that a function take to execute using decorators

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function -{func.__name__} take {end-start}s time")
        return result
    return wrapper

@timer
def execution_time(n):
    time.sleep(1)

execution_time(1)


