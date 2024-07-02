class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        num = x

        while num > 0:
            digit = num % 10 # get the remainder 
            reverse = reverse * 10 + digit
            num //= 10

        return x == reverse
