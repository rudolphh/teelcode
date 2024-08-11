class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}

        for i, num in enumerate(nums):
            if num in diff:
                return [diff[num], i]
            diff[target-num] = i
