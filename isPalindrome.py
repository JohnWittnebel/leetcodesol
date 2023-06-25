class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x is negative, cannot be a palindrome
        if (x < 0):
            return False

        digitArr = []
        while (x > 0):
            digitArr.append(x % 10)
            x = x // 10
        
        revArr = []
        self.myReverse(digitArr, revArr)

        for i in range(len(digitArr)):
            if revArr[i] != digitArr[i]:
                return False
        return True

    
    def myReverse(self, arr, accum):
        if (arr == []):
            return
        else:
            self.myReverse(arr[1:], accum)
            accum.append(arr[0])
