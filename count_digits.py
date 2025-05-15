def fun(n):
    if n ==0: return 0
    return 1+fun(n//10)
print(fun(1234))