
# Question 1:


def double_char(s):
    s1=""
    for i in s:
        s1+=(i*2)
    print(s1)


double_char("1234!_ ")


# Question 2:


def reverse(s):
    if type(s) == bool:
        return not s
    else:
        return "boolean expected"


print(reverse(False))


# Question 3:


def num_layers(n):
    x = 0.5*pow(10,-3)
    return x*pow(2,n)


print(num_layers(21))


# Question 4:


def index_of_caps(s):
    l=[]
    for i in range(len(s)):
        if s[i].isupper():
            l.append(i)
    l.sort()
    return l


print(index_of_caps("sTrinG POol"))


# Question 5:


def find_even_nums(n):
    l=[i for i in range(2,n+1) if i%2==0]
    print(l)


find_even_nums(9)

