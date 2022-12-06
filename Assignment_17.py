# Question 1

guess_me = 7
if guess_me<7:
    print('too low')
elif guess_me>7:
    print('too high')
elif guess_me == 7:
    print('just right')


# Question 2:

guess_me = 7
start = 1
while True:
    if start<guess_me:
        print('too low')
    if start == guess_me:
        print('found it!')
        break
    if start>guess_me:
        print('oops')
        break
    start+=1


# Question 3:

l = [3, 2, 1, 0]

for i in l:
    print(i)

# Question 4:

l = [i for i in range(10) if i % 2 == 0]
print(l)


# Question 5:

d = {i: i ** 2 for i in range(10)}
print(d)


# Question 6:

odd = {i for i in range(10) if i % 2 == 1}
print(odd)


# Question 7:

g = (('Got',i) for i in range(10))
for j in g:
    print(j)


# Question 8:


def good():
    return ["Harry","Ron","Hermione"]


print(good())


# Question 9:


def get_odds():
    for i in range(10):
        if i%3==0:
            yield i


x = get_odds()
l=[j for j in x]
print(l[2])


# Question 10:

class OopsException(ValueError):
    pass


# raise OopsException

try:
    n = int(input('enter a number: '))
    if n<0:
        raise OopsException
except OopsException as e:
    print('caught an oops')


# Question 11:


titles = ["Creature of Habit","Crewel Fate"]
plots = ["A nun turns into a monster","A haunted yarn shop"]

x = zip(titles,plots)

movies = dict(x)
print(movies)
