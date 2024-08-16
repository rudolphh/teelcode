class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1 and target != nums[0]:
            return -1
        elif target == nums[0]:
            return 0

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right sorted portion
            if nums[r] >= nums[mid]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

        