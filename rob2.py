class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: we can use the same solution as before with DP, the only difference is
        #       that we will run that solution excluding the first element and excluding the last
        #       element, this will get us to never rob both the first and last house
        if len(nums) < 2:
            return nums[0]
        maxVal1 = self.robLinear(nums[1:])
        maxVal2 = self.robLinear(nums[:len(nums)-1])
        return max(maxVal1, maxVal2)

    def robLinear(self, nums):
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
