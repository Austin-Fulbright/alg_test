from typing import List
from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        seen = set()
        d = Counter()
        i = 0
        result = 0
        for num in nums:
            if num not in seen:
                count += 1
                seen.add(num)

        for j, x in enumerate(nums):
            d[x] += 1
            while len(d) == count:
                result += len(nums) - j
                
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                     d.pop(nums[i])
                i += 1
        return result

















