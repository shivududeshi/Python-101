
import time
import sys
from project_3 import read_file,validate_args

def union(file_1,file_2):
    """
        finding the union of given two dictionaries

        Args
            file_1,file_2 (dict): dictionaries to find union
        return
            dict: dictionary of union of given dictionaries.
    """
    count_final=len(file_2)
    for x in file_1:
        if x not in file_2:
            file_2[x]=1
            count_final+=1
    return file_2

def write_file(result):
    with open(ret_file,'w') as f3:
        f3.write('\n'.join(result))

if __name__=='__main__':
    time_start = time.time()
    try:
        l1_file,l2_file,ret_file=validate_args(sys.argv)
        l1=read_file(l1_file)
        l2=read_file(l2_file)
        # l2_length=len(l2)
        result=union(l1,l2)
        write_file(result)
        time_end = time.time()
        time_taken = time_end - time_start
        print(f'{l1_file}: {len(l1)} emails, {l2_file}: {len(result)-len(l1)} emails, {ret_file}: {len(result)} emails; Time taken: {time_taken} seconds')
    except Exception as e:
        print('Error is:',e)