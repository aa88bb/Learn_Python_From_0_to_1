def showNum(x):
    return x

print(filter(showNum,range(1,5)))
print(list(filter(showNum,range(1,5))))


def jia(x,y):
    return x+y

from functools import reduce

print(reduce(jia, range(0,10)))

def pf(x):
    return x**x

print(map(pf,range(1,5)))
print(list(map(pf,range(1,5))))