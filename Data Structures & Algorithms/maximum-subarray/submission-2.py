class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=nums[0]
        maximumsum=nums[0]
        for i in range(1,len(nums)):
            currentsum=max(nums[i],currentsum+nums[i])
            maximumsum=max(maximumsum,currentsum)
        return maximumsum
        