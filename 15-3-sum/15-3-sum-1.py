class Solution(object): 
    def threeSum(self, nums): 
        """ 
        :type nums: List[int] 
        :rtype: List[List[int]] 
        """ 

        #  solution O(n^2) time complexity
        
        nums = sorted(nums)
        n = len(nums)
        output = []
        nums = sorted(nums) 
        n = len(nums)
        
        for i in range(n - 2): 
            if nums[i] > 0:
                break
            # since we are going in order, if the previous element is same as this, skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i] 
            left, right = i + 1, len(nums) - 1 
            while left < right: 
                triplet_sum = curr + nums[left] + nums[right] 
                if triplet_sum == 0: 
                    output.append([curr, nums[left], nums[right]] )
                    left += 1
                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                elif triplet_sum > 0: 
                    right -= 1 
                else: 
                    left += 1 
                
        return output