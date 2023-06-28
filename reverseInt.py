class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Idea: use an array to store the digits, then restore it into an integer
        digitArr = []

        # Check for negative value
        if x < 0:
            negative = True
            x *= -1
        else:
            negative = False

        # Edge case
        if x == 0:
            return 0

        # Construct digit Array
        while x > 0:
            digitArr.append(x % 10)
            x = x // 10
        
        # retrieve inverted integer
        retVal = 0
        for i in range(len(digitArr)):
            retVal *= 10
            retVal += digitArr[i]
        if negative:
            retVal *= -1

        # check overflow
        if retVal > pow(2, 31) - 1 or retVal < -1 * pow(2, 31):
            return 0
        else:
            return retVal
