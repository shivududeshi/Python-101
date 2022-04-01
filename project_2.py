
numbers = input('Enter the numbers with comma(,) separation: ').split(',')

# if last digit of number is among (0,,2,4,6,8),then the number is divisible by 2
def div_2(num):
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
    if len(num)==1:
        return num in ['3', '6', '9']
    else:
        digit_list = [int(x) for x in num]
        digit_sum = sum(digit_list)
        num = str(digit_sum)
    return recursive_div_3(num)

def div_4(num):
    if len(num )==1:
        return num in ['0', '4', '8']
    else:
        if div_2(num[-2]):
            return num[-1] in ['0', '4', '8']
        else:
            return num[-1] in ['2', '6']

# if last digit of number is 0 or 5, then that number divisible by 5
def div_5(num):
    return num[-1] in ['0', '5']

# if given number is divisible by 2 and 3 then given number is divisible by 6
def div_6(num):
    return div_2(num) and recursive_div_3(num)


def div_7(num):
    while len(num)!=1:
        num=int(num[:-1])-int(num[-1])*2
        num=str(abs(num))
    return num in ['0','7']

def recursive_div_7(num):
    if len(num)==1:
        return num in ['0','7']
    else:
        num=int(num[:-1])-int(num[-1])*2
        num=str(abs(num))
    return recursive_div_7(num)



def div_8(num):
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


#def div_9(num):
#    while len(num) != 1:
#        digit_list = [int(x) for x in num]
#        digit_sum = sum(digit_list)
#        num = str(digit_sum)
#    return num == '9'

def recursive_div_9(num):
    if len(num)==1:
        return num=='9'
    else:
        digit_list = [int(x) for x in num]
        digit_sum = sum(digit_list)
        num = str(digit_sum)
    return recursive_div_9(num)


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
