import re

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        substr = "" 

        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if len(s[i:j+1]) > len(substr):
                           substr = s[i:j+1]
        return substr 
