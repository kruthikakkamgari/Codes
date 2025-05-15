def knapSackRecur(i, capacity, val, wt):
    if i == len(val):
        return 0
    take = 0
    if wt[i] <= capacity:
        take = val[i] + knapSackRecur(i, capacity - wt[i], val, wt)
    notake = knapSackRecur(i + 1, capacity, val, wt)
    return max(take, notake)

def knapSack(capacity, val, wt):
    return knapSackRecur(0, capacity, val, wt)

val = [1, 1]
wt = [2, 1]
capacity = 3
print(knapSack(capacity, val, wt))