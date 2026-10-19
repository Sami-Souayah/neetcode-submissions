class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def sumofsq(i):
            if i==1:
                return True
            if i in seen:
                return False
            seen.add(i)
            sum = 0
            i = str(i)
            for j in range(len(i)):
                sum += int(i[j])**2
            return sumofsq(sum)
        return sumofsq(n)