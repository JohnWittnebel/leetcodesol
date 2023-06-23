class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Idea: Keep track of the leftmost 0 and swap it with the leftmost non-0
        #.      as we scan from left to right

        zeroIndex = 0
        nonZeroIndex = 0
        while (nonZeroIndex < len(nums) and zeroIndex < len(nums)):
            if nums[zeroIndex] == 0 and nums[nonZeroIndex] != 0:
                if zeroIndex < nonZeroIndex:
                    nums[zeroIndex] = nums[nonZeroIndex]
                    nums[nonZeroIndex] = 0
                nonZeroIndex += 1
            elif nums[zeroIndex] == 0 and nums[nonZeroIndex] == 0:
                nonZeroIndex += 1
            elif nums[zeroIndex] != 0:
                zeroIndex += 1
