class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        maxi = 0

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for k in freq:
            if k - 1 not in freq:
                num = k
                length = 1

                while num + 1 in freq:
                    num += 1
                    length += 1

                maxi = max(maxi, length)

        return maxi