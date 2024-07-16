class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        pre = 1
        for i in range(len(nums)):
            if i == 0:
                output.append(1)
            else:
                pre *= nums[i-1]
                output.append(pre)

        post = 1
        for i in range(len(nums)-1, -1, -1):

            if i == (len(nums) - 1):
                continue
            else:
                post *= nums[i + 1]
                output[i] *= post


        return output