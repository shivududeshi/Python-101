
def read_file(file_name):
    """
        Check for valid mails in given file

        Args
            file_name (str): collection of strings
        return
            dict: dictionary of valid mails as keys.
    """
    import re
    count=0
    # regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@([A-Za-z0-9]+[-])*[A-Za-z0-9]+\.([A-Za-z]{2,})+')

    with open(file_name, 'r') as f:
        valid_mail={}
        for x in f.readlines():
            email = x.rstrip('\n')
            if re.fullmatch(regex, email):
                count += 1
                if email not in valid_mail:
                    valid_mail[email]=1
                else:
                    valid_mail[email] += 1
    return valid_mail,count


def validate_args(argv):
    """
        Check for valid arguments

        Args
            argv (sys.argv): takes arguments from command line
        return
            list: list of valid arguments .
    """
    try:
        output=[]
        for i in range(1,len(argv)):
            with open(argv[i],'r') as f1:
                if type(f1.readline())==str:
                    output.append(argv[i])
    except Exception as e:
        print('Mentioned error occurred.Solve error and rerun programme. the error is: ',e)
    else:
        return output
def write_file(file_3)
    with open(file_3,'w') as f3:
        f3.write('\n'.join())

    time_taken=time_end-time_start
    print(f'{file_1}: {f1_count} emails, {file_2}: {f2_count} emails, {file_3}: {len(result)} emails; Time taken: {time_taken} seconds' )