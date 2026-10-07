class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a = set(s)
        jo = {}
        for i in a:
            ind = s.rindex(i)
            jo[i] = ind
        res = []
        size = 0
        end = 0
        for i, val in enumerate(s):
            size+=1
            if val in jo:
                if jo[val] > end:
                    end = jo[val]
            if i == end:
                res.append(size)
                size = 0
        return res
        