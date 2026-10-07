class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if num in map.keys():
                return [map[num], i]
            diff = target - num
            map[diff] = i
        