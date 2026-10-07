import math
import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        aa = copy.deepcopy(nums)
        for i in nums:
            aa.remove(i)
            result.append(math.prod(aa))
            aa.append(i)
        return result