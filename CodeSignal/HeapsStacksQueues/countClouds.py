"""
Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), 
count the number of clouds. A cloud is surrounded by clear sky, 
and is formed by connecting adjacent clouds horizontally or vertically. 
You can assume that all four edges of the skyMap are surrounded by clear sky.

Example
For

skyMap = [['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']]
the output should be
solution(skyMap) = 2;

For

skyMap = [['0', '1', '0', '0', '1'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '1'],
          ['0', '0', '1', '1', '0'],
          ['1', '0', '1', '1', '0']]
the output should be
solution(skyMap) = 5.
"""
def solution(skyMap):
    def dfs(x, y):
        if x < 0 or x >= len(skyMap) or y < 0 or y >= len(skyMap[0]) or skyMap[x][y] == '0':
            return
        skyMap[x][y] = '0'  # Mark the current cell as visited
        # Explore adjacent cells in all four directions
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    cloud_count = 0  # Initialize cloud count
    # Traverse the grid
    for i in range(len(skyMap)):
        for j in range(len(skyMap[0])):
            if skyMap[i][j] == '1':  # If current cell is a cloud
                cloud_count += 1  # Increment cloud count
                dfs(i, j)  # Explore and mark all cells connected to this cloud
    return cloud_count
