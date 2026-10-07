class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-"
        if strs == [""]:
            return ""
        result = ""
        for i in strs:
            result += i + "-"
        return result
        
        

    def decode(self, s: str) -> List[str]:
        if s == "-":
            return []
        if s == "":
            return [""]
        build = ""
        result = []
        for i in s:
            if i == "-":
                result.append(build)
                build = ""
            else: 
                build+=i

        return result

