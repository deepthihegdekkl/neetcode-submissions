class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        farthest = 0

        while r < len(nums):
            if r > farthest:
                return False

            farthest = max(farthest, r + nums[r])
            
            if farthest >= len(nums) - 1:
                return True

            r += 1

        return True