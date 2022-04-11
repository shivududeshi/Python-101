
import time
import sys
from project_3 import read_file,validate_args,write_file
args = sys.argv

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

if __name__=='__main__':
    time_start = time.time()
    file_1,file_2,file_3=validate_args(args)
    f1_mails=read_file(file_1)
    f2_mails=read_file(file_2)
    result=union(f1_mails,f2_mails)
    write_file(result)
    time_end = time.time()
    time_taken=time_end-time_start
    print(f'{file_1}: {len(f1_mails)} emails, {file_2}: {f2_mails} emails, {file_3}: {len(result)} emails; Time taken: {time_taken} seconds' )