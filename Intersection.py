import time
import sys
from project_3 import email_check
from project_3 import rem_duplicate


time_start = time.time()
file_1=sys.argv[1]
file_2=sys.argv[2]
file_3=sys.argv[3]

count_list=[]
def intersection(file_1,file_2,file_3):
    # function for collecting duplicates from valid email files
    def collect_duplicates(file1,file2):
        # by using dictionary for removing duplicates
        with open(file1, 'r') as f_d:
            with open(file2, 'w') as f_n:
                emails_repeated = {}
                count_duplicates = 0
                for x in f_d.readlines():
                    x = x.strip('\n')
                    if x not in emails_repeated:
                        emails_repeated[x] = 1
                    else:
                        emails_repeated[x] += 1
                        f_n.write(x + '\n')
                        count_duplicates += 1
        return count_duplicates

    count_list.append(email_check(file_1))
    count_list.append(email_check(file_2))
    with open(file_3[:-4] + '_total.txt', 'r+') as f_total:
        rem_duplicate(file_1[:-4]+'_valid.txt')
        rem_duplicate(file_2[:-4]+'_valid.txt')
        with open(file_1[:-4]+'_valid_no_dupl.txt','r') as x_1:
            f_total.write(x_1.read())
        with open(file_2[:-4]+'_valid_no_dupl.txt','r') as x_2:
            f_total.write(x_2.read())
        count_final=collect_duplicates(file_3[:-4] + '_total.txt',file_3)

    time_end = time.time()
    time_taken = time_end - time_start
    print(f'L1.txt: {count_list[0]} emails, L2.txt: {count_list[1]} emails, R.txt: {count_final} emails; Time taken: {time_taken} seconds')

intersection(file_1,file_2,file_3)
# intersection('t1.txt','t2.txt','t3.txt')