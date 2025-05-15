a=int(input())
rem=""
while a:
    rem += str(a%2) 
    a=a//2
print(rem[::-1])
