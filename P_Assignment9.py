# Question 1:


def disarium(n):
    s=0
    l=[]
    j=n
    while n!=0:
        n,b = divmod(n,10)
        l.append(b)
    l=l[::-1]
    for i in range(0,len(l)):
        s+=pow(l[i],i+1)
    return s == j


print(disarium(175))


# Question 2:


for j in range(1,101):
    s=0
    l=[]
    k=j
    while j!=0:
        j,b = divmod(j,10)
        l.append(b)
    l=l[::-1]
    for i in range(0,len(l)):
        s+=pow(l[i],i+1)
    if k == s:
        print(s,end="\t")


# Question 3:


def is_happy(n):
    s=[]
    while n!=1:
        if n in s:
            return False
        s.append(n)
        n = sum(int(i)**2 for i in str(n))
    return True


print(is_happy(19))


# Question 4:


def is_happy():
    for f in range(1,101):
        s=[]
        n=f
        while n!=1:
            if n in s:
                break
            s.append(n)
            n = sum(int(i)**2 for i in str(n))
        else:
            print(f,end="\t")


is_happy()


# Question 5:


def harshad(n):
    l=[]
    j=n
    while n!=0:
        n,b = divmod(n,10)
        l.append(b)
    if j%sum(l)==0:
        return True
    else:
        return False


print(harshad(111))


# Question 6:

import math


def checkPronic(x):
    i = 0
    while i <= (int)(math.sqrt(x)):

        if x == i * (i + 1):
            return True
        i = i + 1

    return False


i = 1
while i <= 100:
    if checkPronic(i):
        print(i, end=" ")
    i = i + 1
