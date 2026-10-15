class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        if num%9==0:
            return 9
        else:
            s=num%9
            return s
        


        