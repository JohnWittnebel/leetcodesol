class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Idea: store a dictionary/hash table for each unique element in nums with the number of 
        #       occurances, and then sort that table based on frequency of occurance

        freqDict = {}
        for ele in nums:
            if ele in freqDict:
                freqDict[ele] += 1
            else:
                freqDict[ele] = 1
        
        sortedDict = sorted(freqDict, key=lambda x: freqDict[x])
        retArr = []
        while len(retArr) < k:
            retArr.append(sortedDict[len(freqDict) - len(retArr) - 1])
        return retArr

