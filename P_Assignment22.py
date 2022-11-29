# Question 1:

def list_operation(x,y,n):
    l=[]
    for i in range(x,y+1):
        if i%n==0:
            l.append(i)
    return sorted(l)


print(list_operation(7,9,2))


# Question 2:

def simon_says(l1,l2):
    if len(l1) == len(l2):
        l1.pop(len(l1)-1)
        l2.pop(0)
        if l1==l2:
            return True
        else:
            return False
    else:
        print('please provide strings with equal length')


print(simon_says([1,1,1],[0,1,1]))


# Question 3:

try:
    def society_name(l):
        s=""
        for i in l:
            s+=i[0].upper()
        for j in sorted(s):
            print(j,end="")


    society_name(["amy","zones","lemar"])

except Exception as e:
    print('something wrong happened')


# Question 4:

try:
    def is_isogram(s):
        if len(list(s)) == len(set(s)):
            return True
        else:
            return False


    print(is_isogram("consecutive"))

except Exception as e:
    print("something went wrong")


# Question 5:


def is_in_order(s):
    if s.isnumeric():
        l = list(set(s))
        l=sorted(l)
        for i in range(len(l)-1):
            if int(l[i])+1 != int(l[i+1]):
                return False
        return True
    if s.isalpha():
        l = list(set(s))
        l=sorted(l)
        for i in range(len(l)-1):
            if ord(l[i])+1 !=ord(l[i+1]):
                return False
        return True
    else:
        print('enter valid string')


print(is_in_order("1233445"))
