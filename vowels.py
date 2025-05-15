num=input().lower()
count=0
for i in range(0,len(num)):
    if (num[i]=="a,e,i,o,u"):
        count+=1
        print(count)