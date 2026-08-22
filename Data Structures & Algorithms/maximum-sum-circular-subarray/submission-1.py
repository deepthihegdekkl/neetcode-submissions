class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax=0
        currmin=0
        total=0
        maxi=nums[0]
        mini=nums[0]
        for n in nums:
            currmax=max(currmax+n,n)
            currmin=min(currmin+n,n)
            total+=n
            maxi=max(maxi,currmax)
            mini=min(mini,currmin)
        return max(maxi,total-mini) if maxi>0 else maxi


        