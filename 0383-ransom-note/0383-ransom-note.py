class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1={}
        for i in magazine:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in ransomNote:
            if i not in freq1 or freq1[i]==0:
                return False
            else:
                freq1[i]-=1
        return True
      