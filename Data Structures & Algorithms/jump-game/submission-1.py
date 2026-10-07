class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1
        i = n-2
        while (i>=0):
            jump = nums[i]
            if i + nums[i] >= goal:
                goal = i
                i -= 1
            else:
                i -= 1
        return goal ==0