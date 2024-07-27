class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def count_non_matching(s):
            if not s:
                return 0
            
            first_char = s[0]
            count = 0
            
            for char in s:
                if char != first_char:
                    count += 1
            
            return count

        left = 0
        right = 1

        longest = 0

        while right < len(s):
            count = count_non_matching(s[left:right+1])
            if count <= k:
                longest = max(longest, len(s[left:right+1]))
                right += 1

            else:
                left +=1 
                right = left + 1

        
        return longest
    
### THIS IS WRONG