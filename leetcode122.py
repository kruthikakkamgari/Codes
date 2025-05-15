def maxProfit(p):
    profit=0
    buy=p[0]
    for i in range(1,len(p)):
        if buy<p[i]:
            profit=profit+(p[i]-buy)
        buy=p[i]
    return profit       
p=[7,1,5,3,6,4]
print(maxProfit(p))