class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Idea: DP, memo table A s.t. A[i] is True iff s[:i+1] is segmentable
        # O(nm) runtime, where n = len(s), m = len(wordDict)

        # init memoization table
        memoTable = []
        for ele in s:
            memoTable.append(False)

        n = len(s)
        m = len(wordDict)
        for i in range(n):
            for j in range(m):
                k = len(wordDict[j])
                if s[:i+1] == wordDict[j]:
                    memoTable[i] = True
                elif s[i+1-k:i+1] == wordDict[j] and memoTable[i-k]:
                    memoTable[i] = True
        return memoTable[n-1]
