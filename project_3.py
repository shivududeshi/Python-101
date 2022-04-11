from os import path
import re
def read_file(file_name):
    """
        Check for valid mails in given file

        Args
            file_name (str): collection of strings
        return
            dict: dictionary of valid mails as keys.
    """
    # regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@([A-Za-z0-9]+[-])*[A-Za-z0-9]+\.([A-Za-z]{2,})+')
    with open(file_name, 'r') as f:
        valid_mail={}
        for x in f.readlines():
            email = x.rstrip('\n')
            if re.fullmatch(regex, email):
                if email not in valid_mail:
                    valid_mail[email]=1
    return valid_mail

def validate_args(argv):
    """
        Check for valid arguments

        Args
            argv (sys.argv): takes arguments from command line
        return
            list: list of valid arguments .
    """
    if len(argv)!=4:
        raise Exception('Need to pass 4 arguments')
    else:
        for i in range(1,4):
            if not path.isfile(argv[i]):
                raise Exception(argv[i]+' file not found')
            if path.getsize(argv[i])==0 and i!=3:
                raise Exception(argv[i]+' Input file is empty')
            if path.getsize(argv[i])>0 and i==3:
                raise Exception(argv[3]+' Output file is not empty')

        return argv[1:]
