def lcs(x,y,m,n):
    if m==0 or n==0:
        return 0
    if x[m-1]==y[n-1]:
        return 1+lcs(x,y,m-1,n-1)
    else:
        return max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))
x="agbcdf"
y="abdklmng"
m=len(x)
n=len(y)