class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxS = 0

        sub_set = set()
        for r in range(len(s)):
            while s[r] in sub_set and l < r:
                sub_set.remove(s[l])
                l += 1
                
            sub_set.add(s[r])
            maxS = max(maxS, r - l + 1)

        return maxS
