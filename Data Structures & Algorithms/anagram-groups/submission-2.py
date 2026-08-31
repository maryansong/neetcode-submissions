class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for x in strs:
            count = [0]*26
            for c in x:
                count[ord(c) - ord("a")] += 1
            if tuple(count) not in groups:
                groups[tuple(count)] = [x]
            else:
                groups[tuple(count)].append(x)
        return list(groups.values())




        