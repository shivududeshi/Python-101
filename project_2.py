
# if last digit of number is among (0,,2,4,6,8),then the number is divisible by 2
def div_2(num):
    """
        Check the divisibility of 'n' by 2

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 2.
    """
    # if '.' in num:
    #     num=num.replace('.','')
    return num[-1] in ['0', '2', '4', '6', '8']

#digits of given number are added till single digit is obtained and if that single digit is present in [3,6,9]
#then the given number is divisible by 3 as list elements are divisible by 3.

#def div_3(num):
#    while len(num) != 1:
#        digit_list = [int(x) for x in num]
#        digit_sum = sum(digit_list)
#        num = str(digit_sum)
#    return num in ['3', '6', '9']

def recursive_div_3(num):
    """
        Check the divisibility of 'n' by 3

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 3.
    """
    if num[0]=='-':
        num=num[1:]
    if '.' in num:
        num=num.replace('.','')
    if len(num)==1:
        return num in ['3', '6', '9']
    else:
        digit_list = [int(x) for x in num]
        digit_sum = sum(digit_list)
        num = str(digit_sum)
    return recursive_div_3(num)

# if given number is single digit then the number must be in [0,4,8] to be divisible by 4.
# if given number is two digits and above,then there are two possibilities to check.
# 1) if ten's place digit is even, then unit's place digit must be in [0,4,8] to be divisible by 4.
# 2) if ten's place digit is odd, then unit's place digit must be in [2,6] to be divisible by 4.

def div_4(num):
    """
        Check the divisibility of 'n' by 4

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 4.
    """
    if num[0]=='-':
        num=num[1:]
    if '.' in num:
        num=num.replace('.','')
    if len(num )==1:
        return num in ['0', '4', '8']
    else:
        if div_2(num[-2]):
            return num[-1] in ['0', '4', '8']
        else:
            return num[-1] in ['2', '6']

# if last digit of number is 0 or 5, then that number divisible by 5
def div_5(num):
    """
        Check the divisibility of 'n' by 5

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 5.
    """
    return num[-1] in ['0', '5']

# if given number is divisible by 2 and 3 then given number is divisible by 6
def div_6(num):
    """
        Check the divisibility of 'n' by 6

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 6.
    """
    return div_2(num) and recursive_div_3(num)

#digits of given number are added till single digit is obtained and if that single digit is present in [0,7]
#then the given number is divisible by 7 as list elements are divisible by 7.

# def div_7(num):
#     while len(num)!=1:
#         num=int(num[:-1])-int(num[-1])*2
#         num=str(abs(num))
#     return num in ['0','7']

def recursive_div_7(num):
    """
        Check the divisibility of 'n' by 7

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 7.
    """
    if num[0]=='-':
        num=num[1:]
    if '.' in num:
        num=num.replace('.','')
    if len(num)==1:
        return num in ['0','7']
    else:
        num=int(num[:-1])-int(num[-1])*2
        num=str(abs(num))
    return recursive_div_7(num)

# if given number is single digit then the number must be in [0,8] to be divisible by 8.
# if given number is two digits then the number must be in multiples of 8 upto 100.
# if given number is three digits and above,then there are two possibilities to check.
# 1) if hundred's place digit is even, then last two digits number must be in multiples to be divisible by 8.
# 2) if hundred's place digit is odd, then (last two digits number+4) must be in multiples to be divisible by 8.

def div_8(num):
    """
        Check the divisibility of 'n' by 8

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 8.
    """
    if num[0]=='-':
        num=num[1:]
    if '.' in num:
        num=num.replace('.','')
    multiples=['00','08','16','24','32','40','48','56','64','72','80','88','96']
    if len(num)==1:
        return num in ['0', '8']
    elif len(num)==2:
        return num in multiples
    else:
        if div_2(num[-3]):
            return num[-2:] in multiples
        else:
            two_digits=int(num[-2:])+4
            return str(two_digits) in multiples


#digits of given number are added till single digit is obtained and if that single digit is 9
#then the given number is divisible by 9.

#def div_9(num):
#    while len(num) != 1:
#        digit_list = [int(x) for x in num]
#        digit_sum = sum(digit_list)
#        num = str(digit_sum)
#    return num == '9'

def recursive_div_9(num):
    """
        Check the divisibility of 'n' by 9

        Args
            n (str): the number to check
        return
            bool: 'True' if 'n' is divisible by 9.
    """
    if num[0]=='-':
        num=num[1:]
    if '.' in num:
        num=num.replace('.','')
    if len(num)==1:
        return num=='9'
    else:
        digit_list = [int(x) for x in num]
        digit_sum = sum(digit_list)
        num = str(digit_sum)
    return recursive_div_9(num)

def divisibility_check():
    """
        Check the divisibility of 'n' by 2,3,4,5,6,7,8,9

        Args
            n (str): the numbers to check
        return
            str: numbers which divides given n.
    """
    numbers = input('Enter the numbers with comma(,) separation: ').split(',')

    #to remove string type from input
    numbers_fi=[]
    for x in numbers:
        try:
            if type(float(x))==float:
                numbers_fi.append(x)
        except Exception:
            pass
    numbers=numbers_fi
    #check divisibility for each number
    for x in numbers:
        x_divisors = []
        if div_2(x):
            x_divisors.append('2')
    #    if div_3(x):
    #       x_divisors.append('3')
        if recursive_div_3(x):
            x_divisors.append('3')
        if div_4(x):
            x_divisors.append('4')
        if div_5(x):
            x_divisors.append('5')
        if div_6(x):
            x_divisors.append('6')
    #    if div_7(x):
    #        x_divisors.append('7')
        if recursive_div_7(x):
            x_divisors.append('7')
        if div_8(x):
            x_divisors.append('8')
    #    if div_9(x):
    #        x_divisors.append('9')
        if recursive_div_9(x):
            x_divisors.append('9')


        if x_divisors==[]:
            print('{}: is not divisible'.format(x))
        else:
            div_str = ','.join(x_divisors)
            print('{}: is divisible by '.format(x) + div_str)
    # if __name__=='__main__':
    #     help(divisibility_check)

divisibility_check()
# help(divisibility_check)