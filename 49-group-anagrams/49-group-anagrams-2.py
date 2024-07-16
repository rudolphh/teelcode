class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        anagram_groups = defaultdict(list)

        count = {}

        for s in strs:
            for letter in s:
                count[letter] = 1 + count.get(letter, 0)

            anagram_groups[count].append(s)

        return anagram_groups.values()
    


    #  optimal O(m * n) where m is the length of strs and n is the average length of each string