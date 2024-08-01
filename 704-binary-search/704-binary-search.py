class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # initialize left to 0, right to last element of nums
        left, right = 0, len(nums) - 1

        while left <= right: #  if looking for insertion we can make left < right and adjust left or right to equal mid
            # calculate the mid point
            mid = (right - left) // 2 + left

            # if mid element equals the target
            if nums[mid] == target:
                return mid #  return the mid index

            elif target > nums[mid]:
                left = mid + 1

            elif target < nums[mid]:
                right = mid - 1

        
        return -1