class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        # loop through the set (not num) because we don't care about duplicates
        for num in num_set:
            if (num-1) not in num_set:
                count = 0
                while (num + count) in num_set:
                    count += 1
                longest = max(longest, count)

        return longest