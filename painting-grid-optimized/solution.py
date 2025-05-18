
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        def _generateValidCols(m: int) -> list:
            validCols = []
            def dfs(pos: int, path: list):
                if pos == m:
                    validCols.append(path[:])
                    return
                for i in range(3):
                    if pos > 0 and path[-1] == i:
                        continue
                    path.append(i)
                    dfs(pos + 1, path)
                    path.pop()
            dfs(0, [])
            return validCols
        validc = _generateValidCols(m)

        def _compatibleRows(validCols: list, n: int) -> int:
            from functools import lru_cache

            compat = {}
            for a in validCols:
                compat[tuple(a)] = []
                for b in validCols:
                    if all(x != y for x, y in zip(a, b)):
                        compat[tuple(a)].append(tuple(b))


            def dfs(pos: int, col: tuple) -> int:
                if pos == n - 1:
                    return 1
                total = 0
                for next_col in compat[col]:
                    total += dfs(pos + 1, next_col)
                return total
            result = 0
            for col in validCols:
                result += dfs(0, tuple(col))
            return result
        result = _compatibleRows(validc, n)
        return result
