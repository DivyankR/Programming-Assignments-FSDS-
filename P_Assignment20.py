# Question 1:


def filter_list(l):
    l1=[i for i in l if type(i) == int]
    return l1


print(filter_list(['python',32.3,{'a':1},{'a','v','b'},12,-1]))


# Question 2:


def add_indexes(l):
    for i in range(len(l)):
        l[i]+=i
    return l


print(add_indexes([0,0,0,0]))


# Question 3:

def cone_volume(r,h):
    pi=22/7
    V = pi*(r*r)*(h/3)
    return round(V,2)


print(cone_volume(15,6))


# Question 4:


def triangular_series(n):
    j,s=0,0
    a,i=1,1
    while i<=n:
        s+=(a*i)
        i+=1
    return s


print(triangular_series(215))


# Question 5:


def missing_num(l):
    n = 1
    for i in sorted(l):
        if n!=i:
            return n
        n+=1


print(missing_num([2,3,4,7,6,5,8,9,10]))