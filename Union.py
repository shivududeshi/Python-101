import time
import sys
from project_3 import email_check
from project_3 import rem_duplicate

time_start = time.time()
file_1=sys.argv[1]
file_2=sys.argv[2]
file_3=sys.argv[3]

count_list=[]
count_final=[]
def union(file_1,file_2,file_3):
    count_list.append(email_check(file_1))
    count_list.append(email_check(file_2))
    with open(file_3[:-4] + '_total.txt', 'r+') as f_total:
        with open(file_1[:-4] + '_valid.txt', 'r') as f1_v:
            f_total.write(f1_v.read())
        with open(file_2[:-4] + '_valid.txt', 'r') as f2_v:
            f_total.write(f2_v.read())
        count_final.append(rem_duplicate(file_3[:-4]+'_total.txt'))

    with open(file_3,'w') as f3:
        with open(file_3[:-4]+'_total_no_dupl.txt','r') as ftotal:
            f3.write(ftotal.read())
    time_end = time.time()
    time_taken=time_end-time_start
    print(f'L1.txt: {count_list[0]} emails, L2.txt: {count_list[1]} emails, R.txt: {count_final[-1]} emails; Time taken: {time_taken} seconds' )

union(file_1,file_2,file_3)
