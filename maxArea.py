class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # Idea: There is a trivial O(n^2) solution of brute-forcing, but we can do this much better
        #       in O(n) by having a left and right pointer that meet up
        currLeftIndex = 0
        currRightIndex = len(height) - 1
        currMax = 0
        currLeft = height[currLeftIndex]
        currRight = height[currRightIndex]
        while currLeftIndex != currRightIndex:
            if min(currLeft, currRight) * (currRightIndex - currLeftIndex) > currMax:
                currMax = min(currLeft, currRight) * (currRightIndex - currLeftIndex)
            if currLeft <= currRight:
                currLeftIndex += 1
                currLeft = height[currLeftIndex]
            else:
                currRightIndex -= 1
                currRight = height[currRightIndex]
        return currMax
