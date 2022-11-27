# Question 1

import numpy as np

try:
    X = [[1,2,3],[7,2,56],[8,3,6]]
    Y = [[3,4,6],[5,7,8],[8,3,2]]

    result = np.array(X)+np.array(Y)
    print(result)

except Exception as e:
    print('please try to enter valid arrays')

# Question 2

import numpy as np
try:
    X = [[1,2,3], [7,2,5], [1,3,6]]
    Y = [[3,4,6],[5,7,8],[8,3,2]]
    Z = np.dot(X,Y)
    print(Z)

except Exception as e:
    print('there is some sort of problem please check!')

# Question 3:

import numpy as np
X = np.array([[1,2],[3,4]])
print(X.transpose())

# Question 4:


class Solution:
    def __init__(self, l):
        l.sort()
        print(l)


obj1 = Solution(["try it","you will","succeed"])

# Question 5:
import string as st


class Solution:
    def __init__(self, l):
        s = ""
        for i in l:
            if i not in st.punctuation:
                s+=i

        print(s)


obj2 = Solution("hey! lon#g %time; no see, hope to see{} y+ou soon")