class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Dictionary to count the frequency of each number
        counts = {}
        # List of empty lists, where index represents frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Count frequency of each number in nums
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # Populate the frequency buckets
        for num, count in counts.items():
            freq[count].append(num)

        result = []
        # Iterate from end of freq to the beginning
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                for value in freq[i]:
                    if len(result) < k:
                        result.append(value)
                        # If we have collected k elements, return the result
                        if len(result) == k:
                            return result

        # If k elements are not found (which should not happen as per problem constraints), return the result
        return result


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2)) 
print(sol.topKFrequent([1], 1)) 