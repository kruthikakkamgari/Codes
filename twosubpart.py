def cs(arr,d):
    totalsum=sum(arr)
    if(totalsum+d)%2!=0:
        return 0
    targetsum=(totalsum+d)//2
    dp=[0]*(targetsum+1)
    dp[0]=1
    for num in arr:
        for j in range(targetsum,num-1,-1):
            dp[j]=dp[j]+dp[j-num]
    return dp[targetsum]
arr=[1,6,11,5]
d=1
print(cs(arr,d))