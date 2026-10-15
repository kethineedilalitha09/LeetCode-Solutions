class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        kv={}
        total=0
        def sod(n):
            total=0
            while n>0:
                digit=n%10
                total+=digit
                n=n//10
            return total

        for i in nums:
            s=sod(i)
            if s not in kv:
                kv[s]=[i]
            else:
                kv[s].append(i)
        ans=-1
        for key in kv:
            if len(kv[key])>=2:
                kv[key].sort(reverse=True)
                ans=max(ans,kv[key][0]+kv[key][1])
        return ans



        