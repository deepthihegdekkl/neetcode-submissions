class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                low = j + 1
                high = len(nums) - 1

                while low < high:
                    total = nums[i] + nums[j] + nums[low] + nums[high]

                    if total > target:
                        high -= 1

                    elif total < target:
                        low += 1

                    else:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[low],
                            nums[high]
                        ])

                        low += 1
                        high -= 1

                        while low < high and nums[low] == nums[low - 1]:
                            low += 1

                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1

        return result
        