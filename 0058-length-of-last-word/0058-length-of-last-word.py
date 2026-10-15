class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li=list(map(str,s.split()))
        l=len(li[-1])
        return l
        