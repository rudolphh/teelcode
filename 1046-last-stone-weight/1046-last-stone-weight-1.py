import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x != y:
                rem_stone = y - x
                heapq.heappush(max_heap, -rem_stone)

        return -max_heap[0] if max_heap else 0
    

def main():
    stones = [2,7,4,1,8,1]
    s = Solution()
    print(s.lastStoneWeight(stones))

if __name__ == "__main__":
    main()