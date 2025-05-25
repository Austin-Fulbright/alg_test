import re

class Solution:
    def countSubstrings(self, s: str) -> int:

        def count_from_center(l: int, r: int) -> int:
            count = 0
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            return count
        count_total = 0
        for i in range(len(s)):
            count_total += count_from_center(i, i)
            count_total += count_from_center(i, i+1)

        return count_total 
