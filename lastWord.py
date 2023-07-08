class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        processingWord = True
        currCount = 0
        for ele in s:
            if ele != " " and processingWord:
                currCount += 1
            elif ele != " " and not processingWord:
                currCount = 1
                processingWord = True
            elif ele == " " and processingWord:
                processingWord = False
        
        return currCount
