class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: to solve this in O(n) time with O(1) space we make the observation that
        #       if we remove two adjacent elements that are different from the array,
        #       the majority element of our smaller array is the same as the majority
        #       element of our initial array. If we have scanned to the end and no two
        #       adjacent elements are different, every element that remains is the majority element
        index1 = 0
        index2 = 1
        # base case
        if len(nums) == 1:
            return nums[0]

        while index2 < len(nums):
            if nums[index1] != nums[index2]:
                nums.pop(index2)
                nums.pop(index1)
                if index1 != 0:
                    index1 -= 1
                    index2 -= 1
            else:
                index2 += 1
                index1 += 1
        return nums[index1]
