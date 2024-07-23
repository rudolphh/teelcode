class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #lower_alnum = ''.join([char for char in s.lower() if char.isalnum()])
        #return lower_alnum == ''.join(reversed(lower_alnum))

        lower = s.lower()
        lower_alnum = filter(lambda x: x.isalnum(), lower)
        return lower_alnum == ''.join(reversed(lower_alnum))

        #lower = s.lower() #  first make all characters lowercase

        # lowercase_chars = []
        # for char in s:
        #     ascii_value = ord(char)
        #     if ascii_value >= 65 and ascii_value <= 90:
        #         lowercase_chars.append(chr(ascii_value + 32))
        #     else:
        #         lowercase_chars.append(char)

        # lowercase_string = ''.join(lowercase_chars)

        # print(lowercase_string)