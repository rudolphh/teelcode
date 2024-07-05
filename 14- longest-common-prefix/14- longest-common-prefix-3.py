class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as the longest common prefix candidate
        lcp = strs[0]
        
        for s in strs[1:]:
            # Update lcp to the common prefix between lcp and the current string
            lcp = self.commonPrefix(lcp, s)
            # If at any point the lcp becomes empty, no need to check further
            if not lcp:
                break

        return lcp
    
    def commonPrefix(self, str1, str2):
        """
        Find the common prefix between two strings.
        """
        min_len = min(len(str1), len(str2))
        
        for i in range(min_len):
            if str1[i] != str2[i]:
                return str1[:i]
        
        return str1[:min_len]