class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for c in s:
            if c not in closed:
                stack.append(c)
            elif not stack or stack[-1] != closed[c]:
                return False
            else:
                stack.pop()

        return not stack