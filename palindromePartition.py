class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # idea: recursion
        currPartition = 0
        currPrefix = ""
        retVal = []

        if (len(s) == 0):
            return [[]]
        elif (len(s) == 1):
            return [[s]]

        for ele in s:
            currPrefix += ele
            currPartition += 1
            if self.isPalindrome(currPrefix):
                subPalindromes = self.partition(s[currPartition:])
                for suffix in subPalindromes:
                    retVal.append([currPrefix] + suffix)
        return retVal

    def isPalindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True
