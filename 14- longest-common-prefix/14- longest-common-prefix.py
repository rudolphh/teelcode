class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""

        # find the smallest string
        max_len = len(strs[0])

        for i in range(1, len(strs)):
            if len(strs[i]) < max_len:
                max_len = len(strs[i])

        for p in range(1, max_len+1):
            end = False
            for i in range(len(strs)):
                prefix = strs[0][0:p]

                if prefix != strs[i][0:p]:
                    end = True
                    break

            if end:
                break
          
            lcp = prefix

        return lcp