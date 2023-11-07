class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Idea: use BFS, setting all adjacent 1's to 0's in a floodfill type algorithm.
        #.      runtime: O(nm)
        numIslands = 0
        Queue = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    Queue.append([row,col])
                    numIslands += 1
                while Queue:
                    ele = Queue.pop()
                    if (grid[ele[0]][ele[1]] == "0"):
                        continue
                    if ele[0] < len(grid)-1 and grid[ele[0]+1][ele[1]] == "1":
                        Queue.append([ele[0]+1, ele[1]])
                    if ele[1] < len(grid[0])-1 and grid[ele[0]][ele[1]+1] == "1":
                        Queue.append([ele[0], ele[1]+1])
                    if ele[0] > 0 and grid[ele[0]-1][ele[1]] == "1":
                        Queue.append([ele[0]-1, ele[1]])
                    if ele[1] > 0 and grid[ele[0]][ele[1]-1] == "1":
                        Queue.append([ele[0],ele[1]-1])
                    grid[ele[0]][ele[1]] = "0"
        return numIslands



