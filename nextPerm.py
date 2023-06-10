class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Idea: we need to find the longest suffix that is sorted in descending order,
        #       and then swap the previous element with the next smallest in the suffix
        #       and sort the remaining elements in the suffix.
        # eg. with the perm [6,4,5,3,2,1], the longest suffix that is sorted in descending order is
        #     [5,3,2,1], so we replace 4 with the next smallest, in this case 5, and sort the rest,
        #     resulting in a list of [6,5,1,2,3,4]

        if (len(nums) == 1):
            return nums
            
        # find longest descending suffix
        suffixLen = self.longestDescendingSuffix(nums)
        
        # special case for if the entire list is sorted in descending order
        if (suffixLen == len(nums)):
            nums.sort()
            return

        # swap element before descending suffix with next smallest element
        currSwap = nums[len(nums) - 1 - suffixLen]
        currInd = len(nums) - suffixLen
        bestInd = currInd
        minLarger = 10000
        while (currInd < len(nums)):
            if (nums[currInd] > currSwap and nums[currInd] < minLarger):
                bestInd = currInd
                mindLarger = nums[currInd]
            currInd += 1
        temp = nums[bestInd]
        nums[len(nums) - 1 - suffixLen] = temp
        nums[bestInd] = currSwap

        # Sort the new suffix
        x = sorted(nums[len(nums) - suffixLen:])
        currIndexNums = len(nums) - suffixLen
        currIndexX = 0
        while currIndexNums < len(nums):
            if (x[currIndexX] != nums[currIndexNums]):
                nums[currIndexNums] = x[currIndexX]
            currIndexNums += 1
            currIndexX += 1

    # returns the length of the longest descending suffix of a list
    def longestDescendingSuffix(self, nums):
        currLen = 1
        currInd = len(nums) - 1
        while (currInd >= 0):
            if (nums[currInd] <= nums[currInd - 1]):
                currLen += 1
                currInd -= 1
            else:
                return currLen
        return len(nums)
