import time
import sys
from project_3 import email_check


time_start = time.time()
file_1=sys.argv[1]
file_2=sys.argv[2]
file_3=sys.argv[3]

count_list=[]
def minus(file1,file2,file3):
    def email_dict(file):
        with open(file, 'r') as f_d:
            email_once = {}
            count = 0
            for x in f_d.readlines():
                x = x.strip('\n')
                if x not in email_once:
                    email_once[x] = 1
        return email_once
    count_list.append(email_check(file1))
    count_list.append(email_check(file2))
    file_2_email_dict=email_dict(file2[:-4]+'_valid.txt')
    with open(file1[:-4]+'_valid.txt','r') as f1_valid:
        with open(file3, 'w') as f3:
            count_final=0
            for email in f1_valid.readlines():
                email=email.strip('\n')
                if email not in file_2_email_dict:
                    f3.write(email+'\n')
                    count_final+=1
                else:
                    continue
    time_end = time.time()
    time_taken = time_end - time_start
    print(f'L1.txt: {count_list[0]} emails, L2.txt: {count_list[1]} emails, R.txt: {count_final} emails; Time taken: {time_taken} seconds')


minus(file_1,file_2,file_3)
# minus('t1.txt','t2.txt','t3.txt')