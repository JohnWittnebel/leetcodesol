class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: make a binary array A where A[i] == 1 if i is in nums. Then scan through A
        #.      and find the longest continuous sequence of 1's. This takes O(n + k) time,
        #       where k is the largest integer in nums.

        # Find max element
        maxEle = -1
        for ele in nums:
            if ele > maxEle:
                maxEle = ele
        
        # initialize binary array
        binArr = []
        for _ in range(maxEle+1):
            binArr.append(0)
        
        # add 1's to binary array
        for ele in nums:
            binArr[ele] = 1
        
        # find longest sequence of 1's
        longestSeq = 0
        currSeq = 0
        for ele in binArr:
            if ele == 1:
                currSeq += 1
            else:
                longestSeq = max(longestSeq, currSeq)
                currSeq = 0
        return max(longestSeq, currSeq)
        


