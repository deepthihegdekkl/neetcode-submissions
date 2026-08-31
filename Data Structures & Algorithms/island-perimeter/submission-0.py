class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1

            # Already visited
            if visited[r][c] == 1:
                return 0

            visited[r][c] = 1

            perimeter = 0

            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r, c - 1)

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    return dfs(r, c)

        return 0
        