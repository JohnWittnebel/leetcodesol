class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Idea: We can have a recursive solution where we get all permutations of
        #       the last n-1 elements and then for each one we insert the first element
        #       into all possible positions.
        #       By the nature of this problem, the runtime is exponential

        # Base Case: There is a single number in the list
        if (len(nums) == 1):
            return [nums]

        # get the recursive solution
        smallerPermutation = self.permute(nums[1:])

        largerPermutation = []
        # insert first element into each possible position of each permutation
        for ele in smallerPermutation:
            for i in range(len(ele) + 1):
                tempEle = copy.copy(ele)
                tempEle.insert(i, nums[0])
                largerPermutation.append(tempEle)
        return largerPermutation
        
