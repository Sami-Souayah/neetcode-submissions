class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def stuff(opened,close,curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if close > opened:
                return

            if opened < n:
                stuff(opened+1, close, curr+"(")
            if close < opened:
                stuff(opened, close+1, curr+")")
        stuff(0,0,"")
        return res