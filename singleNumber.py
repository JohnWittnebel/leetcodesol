class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Idea: add all the numbers together in binary form, without carrying over 1's
        runningVal = 0
        for ele in nums:
            runningVal = runningVal ^ ele
        return runningVal

        
