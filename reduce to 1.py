#you are given  an integer n is to print the minimum number of operations required to reduce n to 1. 
# you can perform only 2 operations in any order and any number of times. 
# you can divide n by x where x should be less than n and n modules x==0
#you can subtract 1 from n

n=int(input())
x=int(input())
reduce=0
integer=0
if  x<n:
    n%x==reduce
    integer=1-reduce
print(integer)


