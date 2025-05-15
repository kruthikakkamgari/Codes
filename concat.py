s1 = input()
s2= input()
i=0
res=""
while i<len(s1) and i<len(s2):
    res+=s1[i]+s2[i]
    i+=1
while i<len(s1):
    res += chr(ord(s1[i]) - 32) 
    i+=1
while i<len(s2):
    res += chr(ord(s2[i])- 32) 
    i+=1
print(res)




 