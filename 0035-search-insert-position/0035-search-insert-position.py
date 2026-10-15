class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
                break
            if nums[i]>target:
                return i
                break
        if nums[-1]<target:
            return len(nums)
        