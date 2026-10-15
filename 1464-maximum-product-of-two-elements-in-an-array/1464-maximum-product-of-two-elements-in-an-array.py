class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp=nums
        temp.sort()
        n1=temp[-1]
        n2=temp[-2]
        return (n1-1)*(n2-1)

