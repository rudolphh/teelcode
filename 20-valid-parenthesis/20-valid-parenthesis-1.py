class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        open_brackets = list(matching_brackets.values())
        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif not stack or stack[-1] != matching_brackets[c]:
                return False
            else:
                stack.pop()

        if stack:
            return False
            
        return True