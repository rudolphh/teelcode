class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            left_right_sum = numbers[left] + numbers[right]
            if left_right_sum == target:
                return [left + 1, right + 1]
            elif left_right_sum < target:
                left += 1
            else:
                right -= 1