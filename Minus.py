
import time
import sys
from project_3 import read_file,validate_args

def minus(file_1,file_2):
    """
        finding minus of given two dictionaries

        Args
            file_1,file_2 (dict): dictionaries to find minus
        return
            dict: dictionary of minus of given dictionaries.
    """
    duplicate_dict={}
    for x in file_1:
        if x not in file_2:
            duplicate_dict[x]=1
    return duplicate_dict

def write_file(result):
    with open(ret_file,'w') as f3:
        f3.write('\n'.join(result))

if __name__=='__main__':
    time_start = time.time()
    try:
        l1_file,l2_file,ret_file=validate_args(sys.argv)
        l1=read_file(l1_file)
        l2=read_file(l2_file)
        result=minus(l1,l2)
        write_file(result)
        time_end = time.time()
        time_taken = time_end - time_start
        print(f'{l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {ret_file}: {len(result)} emails; Time taken: {time_taken} seconds')
    except Exception as e:
        print('Error is:',e)
