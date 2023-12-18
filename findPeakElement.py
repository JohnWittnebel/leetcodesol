class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base cases:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        
        # Recursive case:
        middleEle = len(nums) // 2
        if nums[middleEle - 1] < nums[middleEle] and nums[middleEle + 1] < nums[middleEle]:
            return middleEle
        elif nums[middleEle - 1] < nums[middleEle]:
            return 1 + middleEle + self.findPeakElement(nums[middleEle + 1:])
        else:
            return self.findPeakElement(nums[:middleEle])
