# Question 1:


def evenly_divisible(a,b,n):
    s=0
    for i in range(a,b+1):
        if i%n == 0:
            s+=i
    return s


print(evenly_divisible(1,10,3))


# Question 2:


def correct_signs(s):
    regex = eval(s)
    if regex:
        return True
    else:
        return False


print(correct_signs("14>19>2"))


# Question 3:


def replace_vowels(s,c):
    x = ""
    vowels = ['a','e','i','o','u']
    for i in s:
        if i in vowels:
            x+=c
        else:
            x+=i
    print(x)


replace_vowels("shakespeare", "#")


# Question 4:


def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('enter a positive integer: '))
print(factorial(n))


# Question 5:


def hamming_distance(s1,s2):
    if len(s1)!=len(s2):
        print("enter strings of equal length")
    else:
        i=0
        count=0
        while i<len(s1):
            if s1[i]!=s2[i]:
                count+=1
            i+=1
        return count


print(hamming_distance("abcde","bcdef"))