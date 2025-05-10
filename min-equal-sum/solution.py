from typing import List
from collections import Counter

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1zeros = False
        nums2zeros = False
        sum1 = 0
        sum2 = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                nums1[i] = 1
                nums1zeros = True
            sum1+= nums1[i]

        for i in range(len(nums2)):
            if nums2[i] == 0:
                nums2[i] = 1
                nums2zeros = True
            sum2+= nums2[i]
        if sum2 == sum1:
            return sum2
        if sum2 > sum1:
            if nums1zeros:
                return sum2
            else:
                return -1
        else:
            if nums2zeros:
                return sum1
            else:
                return -1
















