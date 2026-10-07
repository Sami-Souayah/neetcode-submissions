class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def stuff(arr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if arr[i]:
                    continue
                curr.append(nums[i])
                arr[i]=True
                stuff(arr)

                curr.pop()
                arr[i]=False

        stuff([False]*len(nums))
        return res