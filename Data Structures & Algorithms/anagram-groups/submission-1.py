class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicanagrams = {}
        groups = {}
        for x in strs:
            key = tuple(sorted(x))
            if key not in groups.keys():
                groups[key] = [x]
            else:
                groups[key].append(x)
        return list(groups.values())



