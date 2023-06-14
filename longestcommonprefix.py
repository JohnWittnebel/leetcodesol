class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        highestCommonPrefixCount = 0

        shortest = 1000
        for ele in strs:
            if len(ele) < shortest:
                shortest = len(ele)

        for j in range(shortest):
            currChar = strs[0][j]
            isCommon = True
            for i in range(len(strs)):
                if (strs[i][j] != currChar):
                    isCommon = False
            if not isCommon:
                break
            else:
                highestCommonPrefixCount += 1
        
        return strs[0][0:highestCommonPrefixCount]
            
