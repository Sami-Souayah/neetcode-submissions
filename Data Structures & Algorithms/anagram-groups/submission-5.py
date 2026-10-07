class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sorte = "".join(sorted(i))
            res[sorte].append(i)
        return list(res.values())