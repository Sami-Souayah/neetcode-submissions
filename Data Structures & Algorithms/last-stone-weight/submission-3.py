import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(set(stones)) > 1:
            big = heapq.nlargest(2, stones)
            diff = abs(big[0]-big[1])
            stones.remove(big[0])
            stones.remove(big[1])
            if diff > 0:
                stones.append(diff)
        if len(stones) % 2 == 1:
            return stones[0]
        if len(stones)>1:
            return 0
        else:
            return stones[0]
