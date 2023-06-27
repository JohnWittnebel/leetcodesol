class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Idea: We can hash each element of t (with count), and then check each start/end index of s
        #       this will take O(m^2) time. Maybe there is some trick to get O(m), but I cant think
        #       of one atm
        myTable = {}
        for ele in t:
            if ele in myTable:
                myTable[ele][0] += 1
                myTable[ele][1] += 1
            else:
                myTable[ele] = [1,1]
        totalElements = len(t)
        totalElementsStart = len(t)
        
        start = 0
        end = 0
        bestStart = 0
        bestEnd = 0
        minSoFar = len(s) + 1
        while start < len(s):
            while end < len(s) and totalElements > 0:
                if s[end] in myTable and myTable[s[end]][0] > 0:
                    totalElements -= 1
                    myTable[s[end]][0] -= 1
                end += 1
            if totalElements == 0:
                if end - start < minSoFar:
                    bestEnd = end
                    bestStart = start
                    minSoFar = end - start
            start += 1
            end = start
            totalElements = totalElementsStart
            for ele in myTable:
                myTable[ele][0] = myTable[ele][1]
            
        if minSoFar <= len(s):
            return s[bestStart:bestEnd]
        else:
            return ""
