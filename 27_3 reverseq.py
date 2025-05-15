def reverse_first_k(q, k):
    if k > len(q) or k <= 0:
        return q  
    solve(q, k)
    s = len(q) - k
    for i in range(s):
        x = q.pop(0)
        q.append(x)
    return q
def solve(q, k):
    if k == 0:
        return
    e = q.pop(0)
    solve(q, k - 1)
    q.append(e)
queue = list(map(int, input().split()))
k = int(input())
queue = reverse_first_k(queue, k)
print(queue)
