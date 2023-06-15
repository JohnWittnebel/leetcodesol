class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # Idea: Determine the number of flips necessary for the first digit and then
        #       recurse on the remaining digits.

        # Base Case
        if (a == 0 and b == 0 and c == 0):
            return 0

        # Recursive cases
        # Case 1
        if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
            return self.minFlips(a/2, b/2, c/2)
        
        # Case 2
        if (a % 2 == 0 and c % 2 == 0):
            return 1 + self.minFlips(a/2, (b-1)/2, c/2)
        
        # Case 3:
        if (b % 2 == 0 and c % 2 == 0):
            return 1 + self.minFlips((a-1)/2, b/2, c/2)
        
        # Case 4:
        if (c % 2 == 0):
            return 2 + self.minFlips((a-1)/2, (b-1)/2, c/2)
        
        # Case 5:
        if (a % 2 == 0 and b % 2 == 0):
            return 1 + self.minFlips(a/2, b/2, (c-1)/2)
        
        # Case 6:
        return self.minFlips(a//2, b//2, c//2)
