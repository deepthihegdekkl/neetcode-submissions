class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])

        visited = [[0] * c for _ in range(r)]

        count = 0

        def dfs(i, j):

            if i < 0 or j < 0 or i >= r or j >= c:
                return

            if grid[i][j] == "0":
                return

            if visited[i][j] == 1:
                return

            visited[i][j] = 1

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(r):
            for j in range(c):

                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count