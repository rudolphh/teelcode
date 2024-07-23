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
            if self.is_alphanum(s[left]):
                if not s[right].isalnum():
                    right -= 1
                    continue
                else:
                    if s[left].lower() != s[right].lower():
                        return False
            else:
                left += 1
                continue

            left, right = left + 1, right - 1

        return True


    def is_alphanum(self, s):
        return ord(c) in range(48, 58) and ord(c) in range(65, 91) and ord(c) in range(97, 123)