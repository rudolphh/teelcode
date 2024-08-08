import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for e in nums:
            if len(heap) < k or heap[0] < e:
                heapq.heappush(heap, e)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
            

def main():

    nums, k = [3,2,1,5,6,4], 2
    
    print(Solution().findKthLargest(nums, k))


    nums, k = [3,2,3,1,2,4,5,5,6], 4
    print(Solution().findKthLargest(nums, k))



if __name__ == "__main__":
    main()