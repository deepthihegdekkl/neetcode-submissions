class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1freq={}
        s2freq={}
        for i in s1:
            s1freq[i]=s1freq.get(i,0)+1
        for j in range(len(s1)):
            s2freq[s2[j]]=s2freq.get(s2[j],0)+1
        if s1freq==s2freq:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            s2freq[s2[right]]=s2freq.get(s2[right],0)+1
            s2freq[s2[left]]-=1
            if s2freq[s2[left]]==0:
                del s2freq[s2[left]]
            left+=1
            if s1freq==s2freq:
                return True
        return False
        