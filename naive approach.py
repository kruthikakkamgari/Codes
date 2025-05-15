def has_duplicates_naive(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return True
    return False
def has_duplicates_optimized(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False