class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # We can associate each string with its sorted anagram. Then we simply group the strings
        # by their associated strings.

        sortedVals = []
        for ele in strs:
            sortedVals.append(sorted(ele))

        retArr = []
        indexTable = {}
        index = 0
        for ele in sortedVals:
            sortedString = "".join(ele)
            if sortedString not in indexTable:
                retArr.append([])
                indexTable[sortedString] = index
                index += 1
        
        for ele in strs:
            sortedString = "".join(sorted(ele))
            retArr[indexTable[sortedString]].append(ele)
        return retArr
