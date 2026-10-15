class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for i in strs:
            j="".join(sorted(i))
            if j not in l:
                l[j]=[i]
            else:
                l[j].append(i)
        ans=list(l.values())
        return ans
        