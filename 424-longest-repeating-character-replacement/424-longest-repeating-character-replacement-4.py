from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxR = 0
        max_freq_c = 0
        l = 0

        for r in range(len(s)):

            count[s[r]] += 1
            max_freq_c = max(max_freq_c, count[s[r]])

            if (r - l + 1) - max_freq_c > k:
                count[s[l]] -= 1
                l += 1

            maxR = max(maxR, (r - l + 1))
            
        return maxR
