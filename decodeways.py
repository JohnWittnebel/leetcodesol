class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Idea: Use DP with memoization table that has the number of decodings
        #       for the last k characters at index n-k

        # initialize memoization table
        memoTable = []
        n = len(s)
        for _ in range(n):
            memoTable.append(0)
    
        # build memoization table up
        for i in range(n):
            # starting point to prevent index out of bound errors
            if (i == 0) and int(s[n-1]) != 0:
                memoTable[n-1] = 1
                continue

            # case 1: we see a value x, 3 <= x <= 9. There are no additional ways to decode
            if (int(s[n-1-i]) >= 3 and int(s[n-1-i]) <= 9):
                memoTable[n-i-1] = memoTable[n-i]
                continue

            # case 2: we see a value x, x == 0. There are no ways to decode here,
            #         since we are starting with a prefix of 0
            if (int(s[n-1-i]) == 0):
                memoTable[n-i-1] = 0
                continue
            
            # case 3: we see a value x, x == 1. Here x could be a character itself,
            #         or x with the next number could be a character.
            if (int(s[n-1-i]) == 1):
                if (i == 1):
                    memoTable[n-i-1] = memoTable[n-i] + 1
                else:
                    memoTable[n-i-1] = memoTable[n-i] + memoTable[n-i+1]
                continue

            # case 4: x == 2, similar to case 3
            if (int(s[n-1-i]) == 2):
                if (i == 1) and int(s[n-i]) < 7:
                    memoTable[n-i-1] = memoTable[n-i] + 1
                elif (i == 1):
                    memoTable[n-i-1] = 1
                elif (int(s[n-i]) > 6):
                    memoTable[n-i-1] = memoTable[n-i]
                else:
                    memoTable[n-i-1] = memoTable[n-i] + memoTable[n-i+1]

        # return output
        return memoTable[0]

