class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nums_index:
                return([nums_index[diff],i])
            nums_index[nums[i]]=i
        