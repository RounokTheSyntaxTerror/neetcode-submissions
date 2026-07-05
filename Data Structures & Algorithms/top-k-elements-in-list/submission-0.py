class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            frq[num] = frq.get(num,0) + 1

        sorted_nums = sorted(frq.keys(), key=lambda x: -frq[x])
        return sorted_nums[:k]

            
        
                