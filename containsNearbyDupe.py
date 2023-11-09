class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Idea: create a dict A where the keys are numbers in nums, and the value A[i] = k, where k is the highest index found where nums[k] = i
        myDict = {}
        for index in range(len(nums)):
            if nums[index] not in myDict:
                myDict[nums[index]] = index
            elif index - myDict[nums[index]] <= k:
                return True
            else:
                myDict[nums[index]] = index
        return False
        
