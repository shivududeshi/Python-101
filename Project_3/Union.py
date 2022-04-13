import time
import sys
from Sets import read_file, validate_args, write_file, union


if __name__ == '__main__':
    try:
        time_start = time.time()
        l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1, l1_count = read_file(l1_file)
        print(l1)
        l2, l2_count = read_file(l2_file)
        print(l2)
        result = union(l1, l2)
        # write_file(result)
        write_file(result, ret_file)
        time_end = time.time()
        time_taken = time_end - time_start
        print(f'Output: {l1_file}: {l1_count} emails, {l2_file}: {l2_count} emails, {ret_file}: {len(result)} emails; Time taken: {round(time_taken)} seconds')
    except Exception as e:
        print('Error is:', e)
