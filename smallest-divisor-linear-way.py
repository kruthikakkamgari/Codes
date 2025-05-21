from math import*
def smallestDivisor(arr,k):
    for div in range(1,max(arr)+1):
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
        if Sum<=k:
            return div
arr=[1, 2, 9]
k = 6
print(smallestDivisor(arr,k))