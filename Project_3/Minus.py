import time
import sys
from Sets import *


if __name__ == '__main__':
    try:
        time_start = time.time()
        # l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1_file, l2_file, ret_file = 't1.txt', 't2.txt', 'R1.txt'
        l1 = Myset(l1_file)
        l2 = Myset(l2_file)
        result = l1-l2
        result.write_file(ret_file)
        time_end = time.time()
        time_taken = time_end - time_start
        print(f'Output: {l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {ret_file}: {len(result)}\
emails; Time taken: {round(time_taken)} seconds')
    except Exception as e:
        print('Error is:', e)
