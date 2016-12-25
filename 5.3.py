def fun(n):
    for i in range(n):
        yield i



r = fun(3)
print(r.__next__())
print(r.__next__())


g = (x*x for x in range(3,10))

print(g.__next__())
print(g.__next__())