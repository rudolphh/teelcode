import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left = []
            right = []
            mid = []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if len(left) >= k:
                return quickSelect(left, k)
            if (len(left) + len(mid)) < k:
                return quickSelect(right, k - (len(left) + len(mid)))
            
            return pivot

        return quickSelect(nums, k)
            

def main():

    nums, k = [3,2,1,5,6,4], 2
    
    print(Solution().findKthLargest(nums, k))


    nums, k = [3,2,3,1,2,4,5,5,6], 4
    print(Solution().findKthLargest(nums, k))



if __name__ == "__main__":
    main()