from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        if not (a + b > c) & (b + c > a) & (a + c > b):
            return "none"
        elif not (a ^ b) | (b ^ c) | (a ^ c):
            return "equilateral"
        elif not (a ^ b) and (b ^ c) and (a ^ c):
            return "isosolece"
        else:
            return "scalene"
