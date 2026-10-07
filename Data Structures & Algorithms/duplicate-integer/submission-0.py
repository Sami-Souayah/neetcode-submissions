class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        poo = set(nums)
        return len(poo) != len(nums)