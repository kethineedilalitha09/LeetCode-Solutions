class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        a=list(freq.values())
        count=0
        for i in a:
            pair=((i*(i-1))/2)
            count+=pair
            count=int(count)
        return count
