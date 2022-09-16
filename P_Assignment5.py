# Question 1

l = []


def lcm():
    while True:
        x = int(input('enter a number: '))
        l.append(x)
        ch = input("want to enter more? (y/n)")
        if ch == 'y':
            continue
        if ch == 'n':
            break
    m = max(l)
    j = 1
    c = 1
    while True:
        c = m * j
        count = 0
        for i in l:
            if c % i == 0:
                count += 1
        if count == len(l):
            print("{} is the lcm of {}".format(c, l))
            break
        j += 1


lcm()

# Question 2

def hcf():
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    l = [x, y]
    x1 = []
    if x % y == 0 or y % x == 0:
        h = min(l)
    else:
        for i in l:
            j = 1
            while j < i:
                if i % j == 0:
                    x1.append(j)
                j += 1
        for k in x1:
            if x % k == 0 and y % k == 0:
                h = k

    print('hcf of {} and {} is {}'.format(x, y, h))


hcf()

# Question 3

def num_conv(a):
    b = a
    l = []
    while b != 0:
        rem = b % 2
        l.append(rem)
        b = b // 2
    l1 = l[::-1]
    print('binary number for {} is:'.format(a))
    for i in l1:
        print(i, end='')
    print()
    if a < 8:
        print('octal number of {} is {}'.format(a, a))
    else:
        c = a
        lt = []
        while c != 0:
            rem1 = c % 8
            lt.append(rem1)
            c = c // 8
        lt1 = lt[::-1]
        for j in lt1:
            print(j, end='')
    print()
    d = a
    ls = []
    di = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while d != 0:
        rem2 = d % 16
        if rem2 >= 10:
            for k in di:
                if k == rem2:
                    ls.append(di[k])
        else:
            ls.append(rem2)
        d = d // 16
    ls1 = ls[::-1]
    for m in ls1:
        print(m, end='')
    print()


a = int(input('enter the number for conversion: '))
num_conv(a)

# Question 4

n = input('enter the character to find its ascii value: ')
print('the ascii value of {} is {}'.format(n, ord(n)))

# Question 5

def calc(a, b):
    c = input('enter the operation which you want to perform for 2 numbers(enter +,-,*,/):')
    if c == '+':
        print('{} + {} = {}'.format(a, b, (a + b)))
    if c == '-':
        print('{} - {} = {}'.format(a, b, (a - b)))
    if c == '*':
        print('{} * {} = {}'.format(a, b, (a * b)))
    if c == '/':
        try:
            print('{} / {} = {}'.format(a, b, (a / b)))
        except ZeroDivisionError as e:
            print("the denominator can't be zero")


a = int(input('enter first number: '))
b = int(input('enter second number: '))
calc(a, b)


