class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        res = 0
        prev = None
        count = 1
        for i in nums:
            if prev == i:
                continue
            elif prev!= None and prev + 1 == i:
                count+=1
                prev = i
            else:
                if count > res:
                    res = count
                count=1
                prev = i
        return max(res,count)
