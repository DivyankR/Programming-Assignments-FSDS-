# Question 1:

def unique(d):
    l=[]
    for i in d.values():
        l.append(i)
    for i in l:
        if l.count(i)==1:
            print(i,end="\t")


unique({"a":1,"b":1,"c":2,"d":3})


# Question 2:

try:
    def sum_items(d):
        k_sum,v_sum = 0,0
        for i,j in d.items():
            if type(i)==int or type(i)==float:
                k_sum+=i
            if type(j)==int or type(j)==float:
                v_sum+=j
        return k_sum,v_sum


    print(sum_items({"sum":1,'loa':4,'iajs':91}))
except Exception as e:
    print("something is wrong")


# Question 3:

from itertools import product

d={"fruits":["apple","mango","banana"],'order':[1,2,3]}


def flat_dict(d):
    print("original dictionary: ",d)
    res = dict(zip(d['fruits'],d['order']))
    return res


print(flat_dict(d))


# Question 4:


from collections import OrderedDict

d = OrderedDict({'a':1,'b':2,'c':3})

d.update({'d':9})
print('initial dict:',d)

d.move_to_end('d',last=False)

print('resultant dictionary: ',d)


# Question 5:


from collections import OrderedDict


def chckorder(s, p):

    d = OrderedDict.fromkeys(s)

    l = 0
    for i, j in d.items():
        if i == p[l]:
            l = l + 1

        if l == (len(p)):
            return 'true'

    return 'false'


if __name__ == "__main__":
    s = 'bikers block'
    p = 'er'
    print(chckorder(s, p))


# Question 6:


try:
    d={'a':[123.35,12,234],'b':2,'c':3}
    print(d)
    for i in sorted(d):
        print(i,d[i])


except Exception as e:
    print('there is some sort of error')

