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
        previousValue = 0

        for c in s:
            currentValue = symbols[c]

            if previousValue < currentValue:
                total += currentValue - 2 * previousValue
            else:
                total += currentValue

            previousValue = currentValue

        return total
