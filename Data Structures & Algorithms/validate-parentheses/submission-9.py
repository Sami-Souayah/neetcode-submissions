class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "[":"]", "{":"}"}

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