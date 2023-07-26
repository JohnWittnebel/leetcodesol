class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        remainingAsteroidArr = []
        currRemainingCount = 0
        currProcessIndex = 0
        n = len(asteroids)
        while currProcessIndex < n:
            asteroid = asteroids[currProcessIndex]
            if currRemainingCount == 0:
                remainingAsteroidArr.append(asteroid)
                currRemainingCount += 1
                currProcessIndex += 1
                continue
            
            opp = remainingAsteroidArr[currRemainingCount - 1]
            if opp > 0 and asteroid < 0:
                if -1 * asteroid >= opp:
                    remainingAsteroidArr.pop()
                    currRemainingCount -= 1
                if -1 * asteroid <= opp:
                    currProcessIndex += 1
            else:
                remainingAsteroidArr.append(asteroid)
                currRemainingCount += 1
                currProcessIndex += 1
        return remainingAsteroidArr
