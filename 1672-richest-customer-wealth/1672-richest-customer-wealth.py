class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=[]
        total=0
        for row in accounts:
            a.append(sum(row))
        ans=max(a)
        return ans
