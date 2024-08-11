from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freq = [[] for _ in range(len(nums)+1)]

        for num, count in counts.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
