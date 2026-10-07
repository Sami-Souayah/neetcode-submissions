class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        poo = set(nums)
        i = 0
        result = []
        while (i<k):
            big = -1
            count = 0
            for j in poo:
                aa = nums.count(j)
                if aa > count:
                    big = j
                    count = aa
            poo.remove(big)
            result.append(big)
            i+=1
        return result