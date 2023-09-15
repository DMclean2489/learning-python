def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(25)
mytripler = myfunc(35)

print(mydoubler(11))
print(mytripler(11))