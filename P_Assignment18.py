# Question 1:


def filter_list(l):
    l=[i for i in l if type(i)==int]
    for j in l:
        if j<0:
            return 'enter positive integers only'
    return l


print(filter_list([4,5,6,"list","string"]))


# Question 2:


def reverse(s):
    s1=""
    for i in s:
        if i.isupper():
            x=i.lower()
            s1+=x
        if i.islower():
            y=i.upper()
            s1+=y
        if i==" ":
            s1+=" "
    return s1[::-1]


print(reverse("Hello World"))


# Question 3:


def writeyourcodehere(l):
    first = l[0]
    middle = l[1:-1]
    last = l[-1]
    print('first element of the list is: ', first)
    print('middle of the list is: ', middle)
    print('last of the list is: ', last)


writeyourcodehere([3,4,7,-12.356,132,9123])


# Question 4:


def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('enter a positive integer: '))
print(factorial(n))


# Question 5:


def move_to_end(l,c):
    for i in range(len(l)):
        if c == l[i]:
            l.remove(l[i])
            l.insert(len(l), c)
    return l


print(move_to_end([7,8,9,1,2,3,4],9))
