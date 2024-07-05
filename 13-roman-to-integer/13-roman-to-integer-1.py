class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        while s:
            # since we are checking the element next to it, 
            # we have to make sure there is an element next to it
            if len(s) > 1:
                # if the first numeral is greater or equal value, add to total and remove
                if symbols[s[0]] >= symbols[s[1]]:
                    total += symbols[s[0]]
                    s = s[1:]
                # else we subtract the smaller numeral from the larger, add to total and remove
                else:
                    total += symbols[s[1]] - symbols[s[0]]
                    s = s[2:]
            else: # otherwise it is the last element and we can just add to total
                total += symbols[s[0]]
                s = ""

        return total
