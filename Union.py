
import time
import sys
from project_3 import email_check

time_start = time.time()

file_1=sys.argv[1]
file_2=sys.argv[2]
file_3=sys.argv[3]

def union(file_1,file_2,file_3):
    f1_valid_mails,f1_count=email_check(file_1)
    f2_valid_mails,f2_count=email_check(file_2)
    count_final=f2_count
    for x in f1_valid_mails:
        if x not in f2_valid_mails:
            f2_valid_mails[x]=1
            count_final+=1
    with open(file_3,'w') as f3:
        f3.write('\n'.join(f2_valid_mails))
    time_end = time.time()
    time_taken=time_end-time_start
    print(f'L1.txt: {f1_count} emails, L2.txt: {f2_count} emails, R.txt: {count_final} emails; Time taken: {time_taken} seconds' )

union(file_1,file_2,file_3)
# union('L1.txt','L2.txt','R.txt')
