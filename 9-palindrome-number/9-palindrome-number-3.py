class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = ""
        for c in str(x):
            reverse = c + reverse

        if(str(x) == reverse):
            return True
        else:
            return False