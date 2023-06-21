class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Idea: use a dictionary/hash table to store each value and do a simple scan

        myDict = {}
        for ele in nums:
            if ele in myDict:
                return True
            else:
                myDict[ele] = 1
        return False
