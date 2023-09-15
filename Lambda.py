def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(25)

print(mydoubler(13))
