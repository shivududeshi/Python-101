from os import path
import re


def read_file(file_name):
    """
    Check for valid mails in given file

    Args:
        file_name (str): collection of strings

    Returns
        dict: return dictionary of valid mails as keys.
    """
    # regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@([A-Za-z0-9]+[-])*[A-Za-z0-9]+\.([A-Za-z]{2,})+')
    regex = re.compile(r'[A-Za-z]([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z]([A-Za-z0-9]+[-])*[A-Za-z0-9]+\.([A-Za-z]{2,})+')
    with open(file_name, 'r') as f:
        valid_mails = {}
        count = 0
        for x in f.readlines():
            email = x.rstrip('\n')
            if re.fullmatch(regex, email):
                count += 1
                print(email)
                if email.lower() not in valid_mails:
                    valid_mails[email.lower()] = 1
    return valid_mails, count


def write_file(result, out_file):
    """
    Write input to file
    py:function::

    Args:
        result(dict), out_file(text file): dictionary to write into file
    Returns:
        None
    """
    with open(out_file, 'w') as f3:
        f3.write('\n'.join(result))


def validate_args(argv):
    """
    Check for valid arguments
    py:python::

    Args:
        argv(list): takes arguments from command line

    Returns:
        list: return list of valid arguments.
    """
    if len(argv) != 4:
        raise Exception('Usage: python Union.py <in_file1> <out_file2> <result_file>')
    else:
        for i in range(1, 3):
            if not path.isfile(argv[i]):
                raise Exception(argv[i] + ' file not found')
            if path.getsize(argv[i]) == 0:
                raise Exception(argv[i]+' Input file is empty')
            # if path.getsize(argv[i]) > 0 and i == 3:
            #     raise Exception(argv[3]+' Output file is not empty')
        return argv[1:]
