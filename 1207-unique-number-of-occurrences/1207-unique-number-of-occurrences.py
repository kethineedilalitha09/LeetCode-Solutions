class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        a=freq.values()
        if len(a)==len(set(a)):
            return True
        else:
            return False
            