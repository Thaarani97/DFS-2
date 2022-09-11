#TC - O(m*n)
#SC - O(m*n) 
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = deque()
        m = len(mat)
        n = len(mat[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        dist = 1
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = -1
        
        while q:
            size = len(q)
            for _ in range(size):
                x,y = q.popleft()
                for dx,dy in dirs:
                    nr = dx+x
                    nc = dy+y
                    if nr>=0 and nr<m and nc>=0 and nc<n and mat[nr][nc] == -1:
                        q.append([nr,nc])
                        mat[nr][nc] = dist
            
            dist+=1
            
        return mat