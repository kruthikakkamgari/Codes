a=list(map(int,input().split()))
for i in a:
    if i==0:
        a.remove(0)
        a.append(0)
        
print(a)