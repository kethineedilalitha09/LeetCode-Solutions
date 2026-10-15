class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
            num=n
            while True:
                d=list(map(int,str(num)))
                p=1
                for i in d:
                    p*=i
                if p%t==0:
                    return num
                else:
                    num+=1


        