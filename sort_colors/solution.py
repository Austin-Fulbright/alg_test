from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3

        for i in range(len(nums)):
            counts[nums[i]] += 1
        x = 0
        for i in range(3):
            while counts[i] > 0:
                nums[x] = i
                counts[i] -= 1
                x += 1
        print(f"nums: {nums}")


        
















