import time
import os


def print_range(start, end):
    print(os.environ['table_name'])
    for num in range(start, end + 1):
        time.sleep(1)
        print(num)
        # checking condition
        if num % 2 == 0:
            print(num, end=" ")
