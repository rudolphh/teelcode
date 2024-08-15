class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # using O(1) memory - no extra memory needed
        # two pointers, one from left and one from right
        # move them towards each other until they meet in the middle
        # if at any point the characters don't match, return False
        
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alphanum(s[left]):
                left += 1
            while left < right and not s[right]:
                right -= 1

            left, right = left + 1, right - 1

        return True


    def is_alphanum(self, c):
        return ord('0') <= ord(c) <= ord('9') and ord('A') <= ord(c) <= ord('Z') and ord('a') <= ord(c) <= ord('z')