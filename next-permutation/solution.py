from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None: 
        n = len(nums)
        idx = -1 
        for i in range(n-1, 0, -1):
            if nums[i - 1] < nums[i]:
                idx = i-1
                break

        if idx == -1:
            nums.reverse()
            return

        succ = -1
        for j in range(n - 1, idx, -1):
            if nums[j] > nums[idx]:
                succ = j
                break

        nums[idx], nums[succ] = nums[succ], nums[idx]

        nums[idx+1:] = reversed(nums[idx+1:])

