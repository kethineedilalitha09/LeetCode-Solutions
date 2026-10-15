class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime=[True]*n
        prime[0]=prime[1]=False
        count=0
        m=int(n**(0.5))
        for i in range (2,m+1):
            if prime[i]==True:
                for j in range(i*i, n, i):
                    prime[j] = False
        for k in range (2,n):
            if prime[k]==True:
                count+=1
        return count




        