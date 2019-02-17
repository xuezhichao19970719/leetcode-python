class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                elif j!=0 and i!=0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                elif i==0 and obstacleGrid[i][j-1]==1 or j==0 and obstacleGrid[i-1][j]==1 or i == j == 0:
                    obstacleGrid[i][j]=1
        return obstacleGrid[-1][-1]
        