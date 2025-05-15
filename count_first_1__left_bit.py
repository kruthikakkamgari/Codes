a=int(input())
pos=0
length=a.bit_length()
count=0
while a&1==0:
    a=a>>1
    count += 1
pos =length-count
print(pos)


