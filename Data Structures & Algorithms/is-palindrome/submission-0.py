class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        curr = -1
        for i in range(len(s)):
            print(s[i],s[curr])
            if s[i] == s[curr]:
                curr -= 1
                continue
            else:
                return False
        return True