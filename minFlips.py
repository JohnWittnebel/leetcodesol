class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Strategy: 1. find the number of 0's in the string
        #           2. Traverse the string, decrease the value whenever you see a 0, increase by 1
        #              when you find a 1. This will indicate the number of bits needed to flip
        #              given that you change everything to the left of the current index to 0 instead 
        #              of 1. The minimum of all these values will be the answer.

        minSoFar = self.numberZeroes(s)
        currCount = minSoFar
        for item in s:
            if item == "1":
                currCount += 1
            else:
                currCount -= 1
            if minSoFar > currCount:
                minSoFar = currCount
            print(currCount)
        return currCount

    def numberZeroes(self, s):
        count = 0
        for item in s:
            if item == "0":
                count += 1

        print(count)
        return count

x = Solution()
print(x.minFlipsMonoIncr("00101"))

