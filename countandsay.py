class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if (n == 1):
            return "1"
        prev = self.countAndSay(n-1)
        retString = ""
        elementVal = -1
        count = 0
        for ele in prev:
            if count == 0:
                elementVal = ele
                count = 1
            elif elementVal == ele:
                count += 1
            else:
                retString += str(count)
                retString += elementVal
                count = 1
                elementVal = ele
        retString += str(count)
        retString += elementVal
        return retString

