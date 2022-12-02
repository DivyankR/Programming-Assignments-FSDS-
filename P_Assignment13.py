# Question 1:


import math

try:
    def func(s):
        l1=[]
        l = s.split(',')
        for i in l:
            x = math.sqrt((100*int(i)/30))
            l1.append(x)
        for i in l1:
            print(int(i))


    func("100,150,180")
except Exception as e:
    print('enter some valid string separated with comma')


# Question 2:


x = int(input('enter rows number:'))
y = int(input('enter columns number:'))
l=[]

for i in range(x):
    l1=[]
    for j in range(y):
        l1.append(i*j)
    l.append(l1)
print(l)


# Question 3:


def func(s):
    l=s.split(',')
    l.sort()
    for i in range(len(l)):
        if i==len(l)-1:
            print(l[i])
        else:
            print(l[i],',',end='')


func("without,hello,bag,world")


# Question 4:

try:
    def func(s):
        l = s.split()
        l = list(set(l))
        l.sort()
        for i in range(len(l)):
            if i==len(l)-1:
                print(l[i])
            else:
                print(l[i],end=' ')


    func("hello world and practice makes perfect and hello world again")
except Exception as e:
    print('something went wrong')


# Question 5:


def func(s):
    l,d=0,0
    for i in s:
        if i.isalpha():
            l+=1
        if i.isnumeric():
            d+=1
    print("letters: ",l)
    print("digits: ",d)


func("hello world132@!")


# Question 6:
import re

try:

    pass1= input("enter passwords separated by comma: ")
    pass1 = pass1.split(",")

    l = []
    for i in pass1:

        if len(i) < 6 or len(i) > 12:
            continue

        elif not re.search("([a-z])+", i):
            continue

        elif not re.search("([A-Z])+", i):
            continue

        elif not re.search("([0-9])+", i):
            continue

        elif not re.search("([!@$%^&])+", i):
            continue

        else:
            l.append(i)

    print((" ").join(l))

except Exception as e:
    print('something is wrong')