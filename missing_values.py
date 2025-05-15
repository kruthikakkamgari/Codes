
def missing(num): 
    if 0 in num:
        n=len(num)
        missing_num=n*(n+1)//2
         
    else:
        n=len(num)+1
        missing_num=n*(n+1)//2
    actual=sum(num) 
    return missing_num-actual 

num=list(map(int,input().split()))  
print(missing(num))



    

 


