from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        result = [i for i in range(1, n+1)]
        removed = set()
        for num in nums:
            if num not in removed:
                result.remove(num)
                removed.add(num)
        return result 
            

            
        


