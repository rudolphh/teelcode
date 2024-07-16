class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # cheat code: return Counter(s) == Counter(t)
        # another method for O(1) space - possibly sort method (n^2 to nlogn)
        #   depending on built-in library functions for O(1) space 
        # cheat code: return sorted(s) == sorted(t)
        count = {}

        for letter in s:
            count[letter] = 1 + count.get(letter, 0)

        for letter in t:
            if letter in count:
                count[letter] -= 1
            else:
                return False

        for letter in count.keys():
            if count[letter] != 0:  # extra letters will make negative
                return False

        return True