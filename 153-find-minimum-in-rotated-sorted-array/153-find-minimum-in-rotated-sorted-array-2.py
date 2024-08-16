class Solution:
    def findMin(self, nums: list[int]) -> int:
        # when length of nums is 1 or the number at the end of nums
        # is greater than the number on the left of nums
        if len(nums) == 1 or nums[len(nums) - 1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
        
            # we're still in ascending order with respect to mid
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
        
    