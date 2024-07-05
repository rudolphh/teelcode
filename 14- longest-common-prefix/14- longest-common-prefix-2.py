class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Find the minimum length string in the list
        min_length = min(len(s) for s in strs)

        # Initialize the longest common prefix to an empty string
        lcp = ""

        # Compare characters up to the length of the shortest string
        for i in range(min_length):
            # Get the current character from the first string
            current_char = strs[0][i]

            # Check this character against all other strings at position i
            for s in strs:
                if s[i] != current_char:
                    return lcp
            
            # If the character matches all strings, add it to the prefix
            lcp += current_char

        return lcp