class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        poo = {}
        for i in nums:
            if i in poo:
                poo[i] += 1
            else:
                poo[i] = 1
        result = []
        for i in range(k):
            aa = max(poo, key = poo.get)
            result.append(aa)
            poo.pop(aa)
        return result