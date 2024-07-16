class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def isAnagram (s, t):
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

        groups = []

        for word in strs:
            newGroup = True
            for group in groups:
                if isAnagram(word, group[0]):
                    group.append(word)
                    newGroup = False
                    break

            if newGroup:
                groups.append([word])

        return groups