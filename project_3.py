
def email_check(file_name):
    import re
    count=0
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
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
