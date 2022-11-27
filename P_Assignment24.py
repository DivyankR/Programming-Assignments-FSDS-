# Question 1:

def amplify(n):
    l = [i for i in range(1,n+1)]
    x=[]
    for i in l:
        if i % 4 == 0:
            x.append(i*10)
        else:
            x.append(i)
    return x


print(amplify(25))

# Question 2:


def unique(l):
    d={}
    for i in l:
        d[i] = l.count(i)
    for i,j in d.items():
        if j == 1:
            return i


print(unique([3,3,3,7,3,3]))


# Question 3:

pi = 22 / 7


class Circle:
    def __init__(self,r):
        self._r = r

    def getArea(self):
        area = pi*self._r*self._r
        print(int(area))

    def getPerimeter(self):
        pm = 2*pi*self._r
        print(int(pm))


circy = Circle(11)
circy.getPerimeter()
circy.getArea()


# Question 4:


def sorted_by_length(l):
    d={}
    for i in l:
        d.update({len(i):i})
    d = sorted(d.items())
    l.clear()
    for i,j in d:
        l.append(j)
    return l


print(sorted_by_length(["google","apple","facebook","instagram"]))


# Question 5:


def is_triplet(a,b,c):
    l=[a,b,c]
    l.sort()
    if l[0]**2 + l[1]**2 == l[2]**2:
        return True
    else:
        return False


print(is_triplet(1,2,3))