class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #  solution: O(n) time complexity
        #  two pointers, one from left and one from right
        #  move them towards each other until they meet in the middle
        #  calculate the area between them and update max_area if needed
        #  move the pointer with smaller height inwards
        #  return max_area
        
        most = 0
        left, right = 0, len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            water = (right - left) * min_height

            if water > most:
                most = water
            
            if min_height == height[left]:
                left += 1
            else:
                right -= 1

        return most