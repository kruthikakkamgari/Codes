def knapSackRecur(i, capacity, val, wt, memo):
    if i == len(val):
        return 0
    if memo[i][capacity] != -1:
        return memo[i][capacity]
    
    take = 0
    if wt[i] <= capacity:
        take = val[i] + knapSackRecur(i, capacity - wt[i], val, wt, memo)
    
    noTake = knapSackRecur(i + 1, capacity, val, wt, memo)
    memo[i][capacity] = max(take, noTake)
    return memo[i][capacity]

def knapSack(capacity, val, wt):
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(val))]
    return knapSackRecur(0, capacity, val, wt, memo)

val = [1, 1]
wt = [2, 1]
capacity = 3
print(knapSack(capacity, val, wt))