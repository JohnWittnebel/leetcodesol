class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Idea: we will construct a helper array that will indicate that highest point still ahead
        #.      of the current index. This will allow us to ensure that the water from our current
        #.      index onwards can actually be captured.

        highestAheadArr = [0]
        height.reverse()
        currMax = 0
        for ele in height:
            if ele > currMax:
                highestAheadArr.append(ele)
                currMax = ele
            else:
                highestAheadArr.append(currMax)
        highestAheadArr.reverse()
        highestAheadArr = highestAheadArr[1:]
        height.reverse()

        totalRain = 0
        currLevel = 0
        currIndex = 0
        for ele in height:
            if currLevel > ele and highestAheadArr[currIndex] >= ele:
                totalRain += min(currLevel, highestAheadArr[currIndex]) - ele
            elif currLevel < ele:
                currLevel = ele
                if highestAheadArr[currIndex] < currLevel:
                    currLevel = highestAheadArr[currIndex]
            currIndex += 1
        return totalRain
