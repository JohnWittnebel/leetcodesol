class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Idea: Build up the minimum possible from the end to the start, this is O(n) per step
        #       and O(n) total steps, resulting in a O(n^2) solution

        currDist = 0
        distArr = []
        while (currDist < len(nums)):
            if (len(distArr) == 0):
                distArr.append(0)
            else:
                # larger than any possible distance
                currMin = 999999
                distanceToCheck = nums[len(nums) - currDist - 1]
                for i in range(distanceToCheck):
                    if (len(distArr) - i - 1) >= 0:
                        if (distArr[len(distArr) - i - 1] < currMin):
                            currMin = distArr[len(distArr) - i - 1]
                distArr.append(currMin + 1)
            currDist += 1
        return distArr[len(distArr) - 1]

         
