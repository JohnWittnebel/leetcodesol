class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: we can use binary search, but we need to also check the start of the array
        #.      to make sure that we are going to the side with the smallest element
        #. eg. if in the center we see [5, 6, 7], and the first element is 10, we would recurse
        #      on the left, but if the first element was 2, we would rotate on the right side
        #      There is an edge case where there was no rotation, so we need to check that A[0] > A[n-1]
        # Base cases
        n = len(nums)
        if n == 1 or (nums[0] < nums[n-1]):
            return nums[0]
        if n <= 3:
            return min(nums)

        # recursive cases
        pivot = nums[n//2]
        if pivot < nums[n//2 - 1]:
            return pivot
        elif pivot > nums[0]:
            return self.findMin(nums[n//2:])
        else:
            return self.findMin(nums[:n//2])
