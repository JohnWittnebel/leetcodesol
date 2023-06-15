class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Idea: we can take the product of all integers, and then for each element
        #       take the total and divide it by the current value
        #       There is one small problem and that is that 0's will break this,
        #       so we have edge cases to deal with 0's
        
        # if there are at least 2 indices that are 0, every product will be 0
        numZeroes = 0
        outputArr = []
        for ele in nums:
            if ele == 0:
                numZeroes += 1
        if numZeroes >= 2:
            for _ in range(len(nums)):
                outputArr.append(0)
            return outputArr
        
        # here there is at most one 0 in the array, so we will just deal with it individually
        totalProduct = 1
        for ele in nums:
            if ele != 0:
                totalProduct *= ele
        for ele in nums:
            if numZeroes == 1 and ele != 0:
                outputArr.append(0)
            elif ele == 0:
                outputArr.append(totalProduct)
            else:
                outputArr.append(totalProduct / ele)
        return outputArr
