class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            good = target - num
            if good in seen:
                return [seen[good], i]
            seen[num] = i
        return []
