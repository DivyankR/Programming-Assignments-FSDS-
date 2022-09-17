# Question 1

def fib_series(a, b, n):
    if n >= 1:
        print(a, ' ', end='')
        return fib_series(b, a+b, n-1)


n = int(input('enter number of terms in fibonacci series: '))
fib_series(0, 1, n)

# Question 2


def fact(f, n):
    if n >= 1:
        f *= n
        return fact(f, n-1)
    print(f)


n = int(input('enter number for factorial: '))
fact(1, n)

# Question 3

height = float(input('enter the height in meters: '))
weight = float(input('enter the weight in kgs: '))
bmi = weight/(height**2)

if bmi <= 18.5:
    print('{} is your bmi, you are underweight'.format(bmi))
elif (bmi > 18.5) and (bmi < 25):
    print('{} is your bmi, you are normally weighted'.format(bmi))
elif bmi > 25:
    print('{} is your bmi, you are overweight'.format(bmi))

# Question 4

import numpy as np

x = float(input('enter the number: '))
n = np.log(x)
print(n)

# Question 5


def cbe(n):

    cube = 0
    for i in range(1, n+1):
        cube += i**3
        if i < n:
            print('{}^3 + '.format(i), end='')
        if i == n:
            print('{}^3 = '.format(i), end='')

        i += 1
    print(cube)


n = int(input('enter number upto which you want cube: '))
cbe(n)
