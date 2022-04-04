
#function for checking valid mails
def email_check(file):

    def local_check(local):
        if local.isalnum():
            return True
        elif local[0] == '.' or local[-1] == '.':
            return False
        elif [i for i in range(len(local) - 1) if local[i] == local[i + 1] and local[i] in ['.']] != []:
            return False
        elif local.isalnum() == False:
            local_new = local[:]
            for char in local:
                if char in ['.', '_', '-', '!', '&', '+', '#', '$', '%', '\'', '*', '/', '=', '?', '^', '_', '`', '{',
                            '|', '}', '~']:
                    local_new = local_new.replace(char, '')
                    if local_new.isalnum():
                        return True
        else:
            return False

    def domain_check(domain):
        if domain[0] == '-' or domain[-1] == '-':
            return False
        else:
            domain = domain.replace('-', '')
            return domain.isalnum() and len(domain) <= 191

    def tld_check(tld):
        return tld.isalpha() and len(tld) <= 63 and len(tld) >= 2

    count=0
    with open(file, 'r') as f:
        with open(file[:-4] + '_valid.txt', 'w') as v_1:
            # count = 0
            for x in f.readlines():
                email = x.strip('\n')
                email = email.lower()
                if len(email) <= 320 and email.rfind('@') != -1:
                    local = email[:email.rfind('@')]
                    domain_tld = email[email.rfind('@') + 1:]
                    if domain_tld.rfind('.') != -1:
                        domain = domain_tld[:domain_tld.rfind('.')]
                        tld = domain_tld[domain_tld.rfind('.') + 1:]
                    else:
                        continue
                else:
                    continue

                if local_check(local) and domain_check(domain) and tld_check(tld):
                    v_1.write(x)
                    count += 1

    return count

#function for removing duplicates from valid email files
def rem_duplicate(file):
    # by using dictionary for removing duplicates
    with open(file, 'r') as f_d:
        with open(file[:-4] + '_no_dupl.txt', 'w') as f_n:
            email_once = {}
            count = 0
            for x in f_d.readlines():
                x = x.strip('\n')
                if x not in email_once:
                    email_once[x] = 1
                    f_n.write(x + '\n')
                    count += 1
    return count
