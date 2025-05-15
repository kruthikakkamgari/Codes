a=int(input())
a=a[::-1]
count=0
while a&1==1:
    a=a>>1
    count+=1
print(count)