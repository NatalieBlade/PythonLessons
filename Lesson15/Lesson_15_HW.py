some = 0

def var1():
    b = 0
    return b + 5

def var2():
    # global some
    return some + 10
    # print(some)


print(var1())
print(var2())
print(some)


# var1()
# some=var2()
# print(some)


