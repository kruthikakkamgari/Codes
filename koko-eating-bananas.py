from math import*
def kokoEat(arr,k):
    low=0
    high=max(arr)
    while(low<=high):
        bananas=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/bananas)
        if time<=k:
            high=bananas-1
        else:
            low=bananas+1
    return low
arr = [5, 10, 15, 20]
k = 7
print(kokoEat(arr,k))