class Solution:
    def power(self,x,n):
        if n==0:
            return 1
        if n%2==1:
            return x*self.power(x,n-1)
        return self.power(x*x,n//2)
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
        n=abs(n)
        return self.power(x,n)
       