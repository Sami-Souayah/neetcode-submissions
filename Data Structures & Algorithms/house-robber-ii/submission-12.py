class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob(i, end, memo):
            if i>=end:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(rob(i+1, end,memo), nums[i] + rob(i+2, end,memo))
            return memo[i]
        return max(rob(0, len(nums)-1,{}), rob(1, len(nums),{}))