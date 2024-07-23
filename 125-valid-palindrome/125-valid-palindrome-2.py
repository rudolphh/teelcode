class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        lower = s.lower()
        lower_alnum = filter(lambda x: x.isalnum(), lower)
        
        left = 0
        right = len(lower_alnum) - 1

        while left < right:
            if lower_alnum[left] != lower_alnum[right]:
                return False
            left += 1
            right -= 1

        return True
