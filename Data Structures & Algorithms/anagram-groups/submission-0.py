class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            key="".join(sorted(i))
            if key in freq:
                freq[key].append(i)
            else:
                freq[key]=[i]
        return list(freq.values())

        