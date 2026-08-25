class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            if x - arr[left] > arr[right + k - 1] - x:
                left += 1
            else:
                right -= 1

        return arr[left:left + k]