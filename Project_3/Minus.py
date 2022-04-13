import time
import sys
from Sets import *


if __name__ == '__main__':
    try:
        time_start = time.time()
        l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1 = read_file(l1_file)
        l2 = read_file(l2_file)
        result = minus(l1, l2)
        # write_file(result)
        write_file(result, ret_file)
        time_end = time.time()
        time_taken = time_end - time_start
        print(f'Output: {l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {ret_file}: {len(result)} emails; Time taken: {round(time_taken)} seconds')
    except Exception as e:
        print('Error is:', e)
