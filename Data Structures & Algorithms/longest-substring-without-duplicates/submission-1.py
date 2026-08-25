class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        freq={}
        maxi=0
        while right<len(s):
            if s[right] in freq:
                left=max(left,freq[s[right]]+1)
            freq[s[right]]=right
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi


        