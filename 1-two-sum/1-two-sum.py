class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # loop through nums
        difference_at_index = {}
        for index, item in enumerate(nums):
            # if num[i] is a key in the dict 
            if item in difference_at_index.keys() and difference_at_index[item] != index:
                # return dict[num[i], i]
                return [difference_at_index[item], index]

            diff = target - item
            # add target - num[i] as key, index i as value of dict
            difference_at_index[diff] = index
            

# what i learned:
# make the check before adding to the dictionary otherwise you overwrite the index
# of a same number previously encountered