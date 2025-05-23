from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        base = sum(nums)
        deltas = [(x ^ k) - x for x in nums]
        deltas.sort(reverse=True)
        extra = 0
        for i in range(0, len(deltas) - 1, 2):
            pair = deltas[i] + deltas[i+1]
            if pair > 0:
                extra += pair
            else:
                break

        return base + extra
        
            
