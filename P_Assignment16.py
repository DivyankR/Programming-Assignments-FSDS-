# Question 1:

def stutter(s):
    s1=(s[0:2]+"...")*2
    return s1+s+'?'


print(stutter("incredible"))


# Question 2:

def radians_to_degree(n):
    return round(57.2958*n,1)


print(radians_to_degree(20))


# Question 3:


def is_curzon(n):
    if (pow(2,n)+1)%((2*n)+1)==0:
        return True
    else:
        return False


print(is_curzon(10))


# Question 4:


def area_of_hexagon(s):
    const = 1.5*(3**0.5)
    return const*(s**2)


print(area_of_hexagon(2))


# Question 5:


def binary(n):
    s=""
    while n!=0:
        n,b = divmod(n,2)
        s+=str(b)
    s=s[::-1]
    return s


print(binary(15))