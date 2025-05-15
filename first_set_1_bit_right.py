a=int(input())
# count=1 #gives position
count=0  #gives index
while a&1==0:
    a=a>>1
    count+=1
print(count)
 
