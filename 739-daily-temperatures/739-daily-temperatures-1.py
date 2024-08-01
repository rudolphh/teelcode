class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0 for temp in temperatures]
        unanswered = []

        for i, temp in enumerate(temperatures):
                # while there is something in the unanswered stack 
                # and current temp is greater than the stack top temp
                while unanswered and temp > unanswered[-1][1]:
                    # get the index
                    index, _ = unanswered.pop()
                    answer[index] = i - index

                unanswered.append((i, temp))

        return answer