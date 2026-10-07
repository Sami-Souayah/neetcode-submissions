class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [-1,-1,-1]
        for i in triplets:
            if i[0]>target[0] or i[1] > target[1] or i[2]>target[2]:
                continue
            if i[0]==target[0]:
                found[0] = target[0]

            if i[1]==target[1]:
                found[1]=target[1]

            if i[2]==target[2]:
                found[2]=target[2]

        return found==target