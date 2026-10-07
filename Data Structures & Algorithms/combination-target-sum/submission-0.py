class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        def stuff(i, prev):
            if prev == target:
                res.append(curr.copy())
                return
            if prev>target or i>=len(nums):
                return

            curr.append(nums[i])
            stuff(i, nums[i]+prev)

            curr.pop()
            stuff(i+1, prev)

        stuff(0,0)
        return res