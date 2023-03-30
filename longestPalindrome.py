class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Strategy: for now, let us just brute-force check. O(n^3) time, since checking if a pair
        #           of indices is a palindrome takes O(n) time by reversing the list.
        
        reversedString = s[::-1]

        maxSoFar = 0
        maxStartIndex = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if (j - i) > maxSoFar:
                    if (s[i:j] == reversedString[len(s) - j - 1: len(s) - i - 1]):
                        maxSoFar = j - i
                        maxStartIndex = i
        return s[maxStartIndex:maxStartIndex + maxSoFar + 1]

x = Solution()
print(x.longestPalindrome("abcdcbb"))
print(x.longestPalindrome("aaaa"))
print(x.longestPalindrome("abcd"))
print(x.longestPalindrome("ababcbabacababc"))
print(x.longestPalindrome("a"))
