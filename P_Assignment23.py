# Question 1:


def is_symmetrical(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False


print(is_symmetrical(9939))


# Question 2:
import string


def multiply_nums(s):
    l=[]
    c=""
    for i in range(len(s)):
        if s[i] not in string.punctuation :
            c+=s[i]
        if s[i]=='-':
            c+=s[i]
            continue
        if s[i] in string.punctuation:
            l.append(int(c))
            c=""
    l.append(int(c))
    p=1
    for i in l:
        p*=i
    return p


print(multiply_nums("2, -2, 3"))


# Question 3

def square_digits(n):
    l=[]
    while n!=0:
        n,b = divmod(n,10)
        l.insert(0,b)
    x = [i**2 for i in l]
    print(x)
    for i in x:
        print(i,end="")


square_digits(1234)


# Question 4:


def setify(l):
    l=set(l)
    l = list(l)
    l.sort()
    return l


print(setify([3,3,2,1,4]))

# Question 5:


def mean(n):
    l=[]
    while n!=0:
        n,b = divmod(n,10)
        l.append(b)
    s = sum(l)
    return int(s/len(l))


print(mean(9812))
