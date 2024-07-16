class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_encountered = set()
        for num in nums:
            if num in nums_encountered:
                return True
            nums_encountered.add(num)

        return False