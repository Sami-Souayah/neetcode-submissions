class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights)-1
        i=0
        curr = 0
        while (i!=j):
            h = min(heights[i], heights[j])
            w = abs(j-i)
            duh = w*h
            if duh>curr:
                curr = duh
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return curr