class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = defaultdict(list)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for x,y in count.items():
            freq[y].append(x)
            
        freqs = sorted(freq.keys(), reverse=True)
        res = [] 

        
        for i in freqs:
            if len(res) < k:
                res = res + list(freq[i])

        return res

        
