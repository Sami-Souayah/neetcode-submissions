class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "[":"]", "{":"}"}
        if len(s)==0 or len(s)%2 == 1:
            return False
        stc = []
        for i in s:
            if i=="{" or i=="(" or i=="[":
                stc.append(i)
            else:
                if len(stc)==0:
                    return False
                a = stc.pop()
                if pairs[a] != i:
                    return False
               
        return len(stc) == 0