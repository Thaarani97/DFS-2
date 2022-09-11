#TC - O(m*n)
#SC - O(1) 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    count+=1
                    self.dfs(i,j)
        
        return count
                    
                    
    def dfs(self,r,c):
        if r < 0 or r>=self.m or c<0 or c>=self.n or self.grid[r][c] == '0':
            return 

        self.grid[r][c] = '0'
        for dx,dy in self.dirs:
            nr = dx+r
            nc = dy+c
            self.dfs(nr,nc)