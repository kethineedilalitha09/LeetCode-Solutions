class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for key,val in d.items():
            if val>(n/2):
                return key
            
        