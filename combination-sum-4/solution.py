from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = 0
        def dfs (total):
            nonlocal result
            if total > target:
                return
            if total == target:
                result += 1
                return
            for num in nums:
                fuckyou = total + num
                dfs(fuckyou)

            
        for num in nums:
            dfs(num)


        return result
















