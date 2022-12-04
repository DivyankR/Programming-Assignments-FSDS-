# Question 1:

# try:
#     def func(n):
#         p = (i for i in range(n+1) if i%35==0)
#         l = [i for i in p]
#         for i in range(len(l)):
#             if i==len(l)-1:
#                 print(l[i])
#             else:
#                 print(l[i],',',end='')
#
#
#     n = int(input('enter a number: '))
#     func(59)
#
# except Exception as e:
#     print('something went wrong')


# Question 2:


# def func(n):
#     p = (i for i in range(n+1) if i%2==0)
#     l = [i for i in p]
#     for i in range(len(l)):
#         if i==len(l)-1:
#             print(l[i])
#         else:
#             print(l[i],',',end='')
#
#
# n = int(input('enter a number: '))
# func(5)


# Question 3:

# n = int(input('enter number upto which you want series(apart from 1 and 0): '))
# l=[0,1]
#
# [l.append(l[-2]+l[-1]) for i in range(0,n)]
#
# for j in range(len(l)):
#     if j == len(l)-1:
#         print(l[j])
#     else:
#         print(l[j],',',end='')


# Question 4:

# try:
#     email = input('enter the email:')
#     username=""
#     if '@' in email:
#         for i in email:
#             if i == '@':
#                 break
#             else:
#                 username+=i
#
#     else:
#         print('this is not an email id')
#
#     print(username)
#
# except Exception as e:
#     print('something went wrong')


# Question 5:


# class Shape:
#
#     def area(self):
#         area = 0
#
#
# class Square(Shape):
#     def __init__(self,l):
#         self.l = l
#
#     def area(self):
#         area = self.l**2
#         print(area)
#
#
# o = Square(12)
# o.area()
