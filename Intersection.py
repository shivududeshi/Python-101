
import time
import sys
from project_3 import email_check
time_start = time.time()
file_1=sys.argv[1]
file_2=sys.argv[2]
file_3=sys.argv[3]

def intersection(file_1,file_2,file_3):

    f1_valid_mails,f1_count=email_check(file_1)
    f2_valid_mails,f2_count=email_check(file_2)
    duplicate_dict={}
    for x in f1_valid_mails:
        if x in f2_valid_mails:
            duplicate_dict[x]=1
    with open(file_3,'w') as f3:
        f3.write('\n'.join(duplicate_dict))
    time_end = time.time()
    time_taken=time_end-time_start
    print(f'L1.txt: {f1_count} emails, L2.txt: {f2_count} emails, R.txt: {len(duplicate_dict)} emails; Time taken: {time_taken} seconds' )

intersection(file_1,file_2,file_3)
# intersection('L1.txt','L2.txt','R.txt')