class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result=[]
        last={}
        for i in range(len(s)):
            last[s[i]] = i
        l=0
        right=0
        for i in range(len(s)):
            right=max(right,last[s[i]])
            if i==right:
                result.append(right-l+1)
                l=i+1
        return result
        