#write a program to check weather a given number is harshad  number

num=int(input())
temp=num
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num//=10
if temp%sum==0:
    print("harshad")
else:
    print("Not Harshad")
