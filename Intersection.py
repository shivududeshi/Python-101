import time
time_start = time.time()
import sys
from project_3 import email_check,validate_args
args = sys.argv

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

if __name__=='__main__':
    file_1,file_2,file_3=validate_args(args)
    f1_mails,f1_count=email_check(file_1)
    f2_mails,f2_count=email_check(file_2)
    result=intersection(f1_mails,f2_mails)
    with open(file_3,'w') as f3:
        f3.write('\n'.join(result))
    time_end = time.time()
    time_taken=time_end-time_start
    print(f'{file_1}: {f1_count} emails, {file_2}: {f2_count} emails, {file_3}: {len(result)} emails; Time taken: {time_taken} seconds' )