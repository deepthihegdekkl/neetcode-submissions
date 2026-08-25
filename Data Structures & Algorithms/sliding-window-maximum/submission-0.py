from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for right in range(len(nums)):

            # Remove elements smaller than current element
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add current index
            dq.append(right)

            # Remove elements outside the window
            if dq[0] <= right - k:
                dq.popleft()

            # Window has reached size k
            if right >= k - 1:
                ans.append(nums[dq[0]])

        return ans