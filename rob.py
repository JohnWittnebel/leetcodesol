class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Idea: use DP with memoization table A, where A[i] is the maximum value for the input
        #       A[:i]. Runs in O(n) time
        memoTable = []
        for ele in nums:
            memoTable.append(0)
        
        n = len(nums)
        for i in range(n):
            if (i == 0):
                memoTable[i] = nums[i]
            elif (i == 1):
                memoTable[i] = max(nums[0], nums[1])
            else:    
                memoTable[i] = max(nums[i]+memoTable[i-2], memoTable[i-1])
        return memoTable[n-1]
