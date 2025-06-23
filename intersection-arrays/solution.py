from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        seen = defaultdict(int) 
        result = []

        for num in nums1:
            seen[num] += 1
        for num in nums2:
            if seen[num] > 0:
                result.append(num)
                seen[num] -= 1
        return result 


