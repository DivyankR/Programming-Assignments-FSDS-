# Question 1:

def next_in_line(l,n):
    if len(l)==0:
        print('no list has been selected')
    else:
        l.append(n)
        l.pop(0)
        return l


print(next_in_line([],1))


# Question 2:


def get_budgets(l):
    b = 0
    for i in range(len(l)):
        b+=l[i]['budget']
    return b


print(get_budgets([{"name": "John", "age": 21,"budget": 23000},
                   {"name":"Kingsley","age":34,"budget":40000},
                   {"name":"Ron","age":31,"budget":2500}]))


# Question 3:


def alphabet_soup(s):
    l = list(s)
    l.sort()
    s1=""
    for i in l:
        s1+=i
    return s1


print(alphabet_soup("hello"))


# Question 4:


def compound_interest(p,t,r,n):
    total_amount = p*(1+(r/n))**(n*t)
    return total_amount


p = int(input('enter principal amount:'))
t = int(input('enter time in years:'))
r = float(input('enter rate of interest(after conversion of percentage):'))
n = int(input('enter the number of compounding periods:'))
print(compound_interest(p,t,r,n))


# Question 5:


def return_only_integer(l):
    l1 = [i for i in l if type(i) == int]
    return l1


print(return_only_integer([1,'hello',{'a':1},4.5,-1,123,{9,3,1}]))