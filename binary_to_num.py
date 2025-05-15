a=input()
a=a[::-1]
dec=0
for i in range(len(a)):
    dec+=int(a[i])*(2**i)
print(dec)