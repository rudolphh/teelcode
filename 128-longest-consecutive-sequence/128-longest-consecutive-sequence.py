class Solution(object):
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_int: set[int] = set(nums)
        max_count: int = 0

        for num in nums:
            if (num - 1) not in unique_int:
                length: int = 1
                while (num + length) in unique_int:
                    length += 1

                max_count = max(max_count, length)

        return max_count