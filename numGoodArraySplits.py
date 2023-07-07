class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Idea: Use DP with memoization table A s.t. A[i] is the number of way to split nums[i:]
        #.      into good subarrays

        memoTable = []
        n = len(nums)
        for _ in range(n):
            memoTable.append(0)

        seenOne = False
        previousOneIndex = n
        for i in reversed(range(n)):
            if i == n-1:
                memoTable[i] = 1
                if nums[i] == 1:
                    previousOneIndex = n-1
                    seenOne = True
            elif nums[i] == 0:
                memoTable[i] = memoTable[i+1]
            elif previousOneIndex == n:
                memoTable[i] = 1
                previousOneIndex = i
                seenOne = True
            else:
                memoTable[i] = memoTable[i+1]
                currIndex = i+1
                while (currIndex < previousOneIndex):
                    memoTable[i] += memoTable[currIndex+1]
                    currIndex += 1
                memoTable[i] = memoTable[i] % (pow(10,9) + 7)
                previousOneIndex = i
        if seenOne:
            return memoTable[0]
        return 0
