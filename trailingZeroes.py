class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        currFact = 1
        trailingZeroes = 0
        while n > 1:
            currFact *= n
            while currFact % 10 == 0:
                currFact /= 10
                trailingZeroes += 1
            n -= 1
        return trailingZeroes
                

