# Question 1

def equal(a,b,c):
    l=[a,b,c]
    if len(l) == len(set(l)):
        return 0
    else:
        count = 1
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i] == l[j]:
                    count+=1
        return count


print(equal(5,6,6))

# Question 2:

def dict_to_list(d):
    l = list(d.items())
    return sorted(l)


print(dict_to_list({'likes':212,'dislikes':35,'b':42}))

# Question 3:

def mapping(l):
    d={}
    for i in l:
        d[i] = i.upper()
    print(d)


mapping(['a','b','u','z','x'])

# Question 4:

def vow_replace(s,c):
    x = ""
    vowels = ['a','e','i','o','u']
    for i in s:
        if i in vowels:
            x+=c
        else:
            x+=i
    print(x)


vow_replace("apples and bananas","u")


# Question 5:

def ascii_capitalize(s):
    for i in s:
        if ord(i)%2==0:
            print(i.upper(),end="")
        else:
            print(i.lower(),end="")


ascii_capitalize("THE LITTLE MERMAID")