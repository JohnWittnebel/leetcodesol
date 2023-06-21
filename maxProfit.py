class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Idea: this problem is very similar to the max sum subarray problem.
        #.      we will keep track of the highest value to the right of the lowest value
        #       we have seen until we see a new low.
        currInd = 1
        currMin = prices[0]
        currMax = prices[0]
        currMaxDiff = 0
        while currInd < len(prices):
            if prices[currInd] > currMax:
                currMax = prices[currInd]
            elif prices[currInd] < currMin:
                if (currMax - currMin > currMaxDiff):
                    currMaxDiff = currMax - currMin
                currMin = prices[currInd]
                currMax = prices[currInd]
            currInd += 1
        return max(currMaxDiff, currMax - currMin)
