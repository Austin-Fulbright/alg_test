from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            diff = sum(1 for x,y in zip(a,b) if x!=y)
            return diff == 1
        n = len(words)
        dp = {}

        current_max = []
        def dfs(p1: int, p2: int) -> List[str]:
            if p2 == n:
                return []
            best_tail = dfs(p1, p2+1)

            if groups[p1] != groups[p2] and hamming(words[p1], words[p2]):
                take_tail = [words[p2]] + dfs(p2, p2+1)
                if len(take_tail) > len(best_tail):
                    best_tail = take_tail
            return best_tail


        for i in range(n):
            current = [words[i]]
            if i < n - 1:
                current += dfs(i, i+1)
            if len(current) > len(current_max):
                current_max = current
        return current_max 
