
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

            def dfs(pos: int, path: list) -> int:
                if pos == n:
                    return 1
                total = 0
                for cols in validCols:
                    valid = True
                    for i, num in enumerate(cols):
                        if pos > 0 and num == path[-1][i]:
                            valid = False
                    if valid:
                        path.append(cols)
                        total += dfs(pos + 1, path)
                        path.pop()
                return total
            return dfs(0, [])
        result = _compatibleRows(validc, n)
        return result
