class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currInd = 0
        replaceInd = 1
        currVal = nums[0]
        while (currInd < len(nums)):
            if (nums[currInd] != currVal):
                nums[replaceInd] = nums[currInd]
                replaceInd += 1
                currVal = nums[currInd]
            currInd += 1
        return replaceInd
