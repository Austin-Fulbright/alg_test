import re

class Solution:
    def isPalindrome(self, s: str)-> bool:
        pattern = re.compile(r'[^A-Za-z0-9]+')
        clean = lambda s: pattern.sub('', s)
        s = clean(s).lower()


        return s == s[::-1] 

