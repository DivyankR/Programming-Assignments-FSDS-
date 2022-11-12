# Question 1

# l = []
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# print("the sum of elements in the list is: ",sum(l))


# Question 2

# m=1
# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# for i in l:
#     m*=i
#
# print("the multiplication of elements i the list is: ",m)

# Question 3

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# print("the smallest element in the list is: ",min(l))


# Question 4

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# print("the largest element in the list is: ",max(l))


# Question 5

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# v = sorted(l,reverse=True)
# print(v)
# i=1
# while i<len(v):
#     if v[0]>v[i]:
#         break
#     i+=1
#
# print('the second-highest number in the list is: ', v[i])


# Question 6:

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# s = set(l)
# s = list(s)
# s.sort(reverse=True)
# print(s)
#
# while True:
#     n = int(input('enter the n for nth largest number:'))
#     if n==0 and n==1 and n<0:
#         print('enter another positive number')
#     if 1 < n <= len(s):
#         break
#     else:
#         print('please enter valid n')
#
# print("the {} largest number is: {}".format(n,s[n-1]))


# Question 7

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# print(l)
# for i in l:
#     if i%2 == 0:
#         print(i,end="\n")

# Question 8

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# print(l)
# for i in l:
#     if i%2 == 1:
#         print(i,end="\n")

# Question 9:

# input_l = [[1,35,3],[],{"i":1},{1,2,3}]
# print(input_l)
#
#
# def remove_emptylist(l):
#     for i in input_l:
#         if type(i) == list and len(i) == 0:
#             input_l.remove(i)
#     return input_l
#
#
# x = remove_emptylist(input_l)
# print(x)


#Question 10

# l=["apple",346,{4:23,"seer":3}]
# x = l.copy()
# print(x)


#Question 11:

# l=[]
# while True:
#     try:
#         n = int(input('enter the number for array:'))
#         l.append(n)
#     except Exception as e:
#         print('try to enter integer value')
#     c = input('want to enter more numbers in array?(press n for no): ')
#     if c == 'n' or c == 'N':
#         break
#
# print('the list is:',l)
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
#
# print(d)