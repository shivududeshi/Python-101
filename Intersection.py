import time
import sys
from project_3 import read_file,validate_args

def intersection(file_1,file_2):
    """
        finding the intersection of given two dictionaries

        Args
            file_1,file_2 (dict): dictionaries to find intersection
        return
            dict: dictionary of intersection of given dictionaries.
    """
    duplicate_dict={}
    for x in file_1:
        if x in file_2:
            duplicate_dict[x]=1
    return duplicate_dict

def write_file(result):
    with open(ret_file,'w') as f3:
        f3.write('\n'.join(result))
#
# if __name__=='__main__':
#     time_start = time.time()
#
#     file_1,file_2,file_3=validate_args(sys.argv)
#     f1_mails=read_file(file_1)
#     f2_mails=read_file(file_2)
#     result=intersection(f1_mails,f2_mails)
#     write_file(result)
#     time_end = time.time()
#     time_taken=time_end-time_start
#     print(f'{file_1}: {len(f1_mails)} emails, {file_2}: {len(f2_mails)} emails, {file_3}: {len(result)} emails; Time taken: {time_taken} seconds' )
#
if __name__=='__main__':
    time_start = time.time()
    try:
        l1_file,l2_file,ret_file=validate_args(sys.argv)
        l1=read_file(l1_file)
        l2=read_file(l2_file)
        result=intersection(l1,l2)
        write_file(result)
        time_end = time.time()
        time_taken = time_end - time_start
        print(f'{l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {ret_file}: {len(result)} emails; Time taken: {time_taken} seconds')
    except Exception as e:
        print('Error is:',e)