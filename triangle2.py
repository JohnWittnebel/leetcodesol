class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Idea: From any node, the shortest path to the bottom is the shortest of the
        #       left and right paths plus the current value. We can use a helper to indicate the
        #       node we are currently at and use a simple double recursive call. But, 
        #       this will take exponential time. A better method is to start at the bottom and find 
        #       the shortest route to any given node, working our way up. This makes it so that 
        #       any given node is only doing constant work, so we get linear time.

        currShortest = []
        n = len(triangle)
        for _ in range(n+2):
            currShortest.append(0)

        for i in range(n):
            currShortest = self.minimumTotalHelper(triangle, currShortest, n-i)

        return currShortest[0]

    def minimumTotalHelper(self, triangle, currShortest, currLevel):
        print(currLevel)
        print(currShortest)
        newCurrLevel = []
        for i in range(currLevel):
            print(i)
            if currShortest[i] < currShortest[i+1]:
                newCurrLevel.append(currShortest[i] + triangle[currLevel-1][i])
            else:
                newCurrLevel.append(currShortest[i+1] + triangle[currLevel-1][i])
        return newCurrLevel

