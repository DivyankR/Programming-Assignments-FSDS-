# Question 1:

try:
    class generate:
        def __init__(self,n):
            self.n = n
            x = (i for i in range(1,n+1) if i%7==0)
            for j in x:
                print(j)


    n = int(input('enter a number: '))
    obj = generate(n)

except Exception as e:
    print('something went wrong')


# Question 2:

class sol:
    def __init__(self, s):
        x = s.split()
        d={}
        for i in x:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i,j in d.items():
            print(i,': ',j)


s = input('enter a string: ')
o = sol(s)


# Question 3:

class Person:
    def getGender(self):
        print('hi')


class Male(Person):
    def getGender(self):
        return 'male'


class Female(Person):
    def getGender(self):
        return 'female'


o = Female()
print(o.getGender())


# Question 4:

s=["I", "You"]
v=["Play", "Love"]
o=["Hockey","Football"]
for i in range(len(s)):
    for j in range(len(v)):
        for k in range(len(o)):
            sentence = "%s %s %s." % (s[i], v[j], o[k])
            print(sentence)


# Question 5:

import zlib
s = 'hello world!hello world!hello world!hello world!'
x = bytes(s,'utf-8')
s1 = zlib.compress(x)
print(s1)
print(zlib.decompress(s1))


# Question 6:


def binary(array, tar):
    lower = 0
    upper = len(array)
    print('Length:',upper)
    while lower < upper:
        x = (lower + upper) // 2
        print('Mid Value:',x)
        val = array[x]
        if tar == val:
            return x
        elif tar > val:
            lower = x
        elif tar < val:
            upper = x


l = [345,34,12,678,23,5,8,2]
l.sort()
print('The Value Found at Index:', binary(l, 12))
