class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        for i in range(len(numbers)):
            poo = target - numbers[i]
            if poo in numbers:
                return [i+1,numbers.index(poo)+1]
        return []