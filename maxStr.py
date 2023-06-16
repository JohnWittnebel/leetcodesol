class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The answer should include every positive integer, and the largest
        # even number of odd integers

        pos = []
        negs = []
        zeros = 0
        for ele in nums:
            if ele > 0:
                pos.append(ele)
            elif ele < 0:
                negs.append(ele)
            else:
                zeros += 1
        negs.sort()

        # Edge case where there is only a single odd values, we should return it
        if len(pos) == 0 and len(negs) <= 1 and zeros == 0:
            return negs[0]
        if len(pos) == 0 and len(negs) <= 1:
            return 0
        
        # in every other case, the max value will be non-negative
        retVal = 1
        for ele in pos:
            if ele > 0:
                retVal *= ele
        odd = 0
        for ele in negs:
            if odd == 0:
                odd = ele
            else:
                retVal *= odd
                retVal *= ele
                odd = 0

        return retVal
