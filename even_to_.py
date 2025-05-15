

a = list(map(int, input().split()))
k= []
for i in a:
    if i % 2 != 0:
        temp=a.pop(i)
        a.insert(k,temp)
        k+=1


print(k)



