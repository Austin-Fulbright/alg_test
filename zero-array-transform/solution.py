from typing import List

class Solution:
    def isZeroArray(self, nums: List[str], queries: List[List[int]]) -> List[str]:
        n = len(nums)
        nq = len(queries)
        diff = [0 for _ in range(n + 1)]
        cover = [0 for _ in range(n)]
        coverval = 0

        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        for i in range(n):
            coverval += diff[i]
            cover[i] = coverval

        
        for i in range(n):
            if nums[i] > cover[i]: 
                return False
        return True 
