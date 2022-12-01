# Question 1:

try:
    def func(l):
        for i in l:
            if len(i)>len(l):
                print(i,end="\t")


    func(["forticlient", "words", "input"])
except Exception as e:
    print("please try to provide valid input")


# Question 2:


def remove_char(s,i):
    l=list(s)
    if i>len(s):
        print('please enter valid index')
    l.pop(i-1)
    s1=""
    for i in l:
        s1+=i
    return s1


print(remove_char("among us",6))


# Question 3:

class solution:
    def __init__(self,s):
        self.s = s
        x = s.split()
        print(x)
        p = " ".join(x)
        print(p)


obj = solution("welcome to the jungle")


# Question 4:

def bin_string(s):
    for i in s:
        if i!='0' and i!='1':
            return False
    return True


print(bin_string('101001000101'))


# Question 5:

s1 = input("enter first string: ")
s2 = input("enter second string: ")

l1 = s1.split()
l2 = s2.split()
x=[]

for i in l1:
    if i not in l2:
        x.append(i)

for i in l2:
    if i not in l1:
        x.append(i)

print('uncommon words in the strings are: ',x)


# Question 6:


def duplicate(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,j in d.items():
        if j>=2:
            print(i,end="\t")


duplicate("chromosome")


# Question 7:
import string


def special_char(s):
    var = string.punctuation
    for i in s:
        if i in var:
            return True
    return False


print(special_char("hello#$@ my friend"))