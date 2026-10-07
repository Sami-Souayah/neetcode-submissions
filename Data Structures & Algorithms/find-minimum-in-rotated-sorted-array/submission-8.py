class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                if nums[i] < nums[i-1]:
                    return nums[i]
                if nums[i] > nums[i-1]:
                    i-= 1
                    continue
            if nums[i] > nums[i+1]:
                i += 1
                continue
        return nums[-1]