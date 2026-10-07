import math
import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        poo = copy.deepcopy(nums)
        for i in nums:
            poo.remove(i)
            aa = math.prod(poo)
            poo.append(i)
            result.append(aa)
        return result