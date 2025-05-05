from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        count = 0
        step = 1
        last_dif = None 

        for i in range(1, n):
            dif = nums[i] - nums[i - 1]
            if last_dif == dif:
                count += step
                step += 1
            else:
                step = 1
            last_dif = dif
        
        return count
