# Question 1

array = []
while True:
    try:
        n = int(input('enter the number for array:'))
        array.append(n)
    except Exception as e:
        print('try to enter integer value')
    c = input('want to enter more numbers in array?(press n for no): ')
    if c == 'n' or c == 'N':
        break

print('the array is: ', array)
s = 0
for i in array:
    s += i

print('the sum of elements in array: ', s)

# Question 2

a = []

while True:
    try:
        n = int(input('enter the number for array:'))
        a.append(n)
    except Exception as e:
        print('try to enter integer value')
    c = input('want to enter more numbers in array?(press n for no): ')
    if c == 'n' or c == 'N':
        break

print(a)
for j in a:
    if j == max(a):
        print(j, ' is the largest element in the array')

# Question 3


a = []

while True:
    try:
        n = int(input('enter the number for array:'))
        a.append(n)
    except Exception as e:
        print('try to enter integer value')
    c = input('want to enter more numbers in array?(press n for no): ')
    if c == 'n' or c == 'N':
        break

print(a)

x = int(input('enter the number of left rotations u want to be performed: '))
while x > 0:
    f = a.pop(0)
    a.append(f)
    x -= 1
print("the rotated array is: ", a)

# Question 4

a = []

while True:
    try:
        n = int(input('enter the number for array:'))
        a.append(n)
    except Exception as e:
        print('try to enter integer value')
    c = input('want to enter more numbers in array?(press n for no): ')
    if c == 'n' or c == 'N':
        break

x = 0
while x != len(a)//2:
    f = a.pop(0)
    a.append(f)
    x += 1

print(a)


# Question 5

a = []

while True:
    try:
        n = int(input('enter the number for array:'))
        a.append(n)
    except Exception as e:
        print('try to enter integer value')
    c = input('want to enter more numbers in array?(press n for no): ')
    if c == 'n' or c == 'N':
        break

if sorted(a) == a or sorted(a,reverse=True) == a:
    print("the array {} is monotonic".format(a))
else:
    print("non monotonic")
