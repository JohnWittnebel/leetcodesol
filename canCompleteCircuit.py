class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # idea: cycle through and find the largest negative sum
        #       from the start. If there is a solution, it must start immediately after

        currIndex = 0
        currSum = 0
        largestNeg = 0
        largestNegIndex = 0
        while currIndex < len(gas):
            currSum += (gas[currIndex] - cost[currIndex])
            if currSum < largestNeg:
                largestNeg = currSum
                largestNegIndex = currIndex
            currIndex += 1

        if currSum < 0:
            return -1
        if largestNeg < 0:
            return largestNegIndex + 1
        else:
            return 0

        

