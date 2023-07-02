class Solution(object):
    def minWindow(self, s, t):
        # Idea: We can hash each element of t (with count), and then move a start/end pointer from
        #.      left to right of the array until we find the best soln
        myTable = {}
        for ele in t:
            if ele in myTable:
                myTable[ele] += 1
            else:
                myTable[ele] = 1
        totalElements = len(t)
        totalElementsStart = len(t)
        
        start = 0
        end = 0
        bestStart = 0
        bestEnd = 0
        minSoFar = len(s) + 1
        while start < len(s) and end < len(s):
            if (totalElements == 0):
                if end - start < minSoFar:
                    bestStart = start
                    bestEnd = end
                    minSoFar = end - start
                if s[start] in myTable:
                    myTable[s[start]] += 1
                    if (myTable[s[start]] > 0):
                        totalElements += 1
                start += 1
            elif s[end] in myTable:
                myTable[s[end]] -= 1
                if myTable[s[end]] >= 0:
                    totalElements -= 1
                end += 1
            else:
                end += 1
            
        while (totalElements == 0):
            if end - start < minSoFar:
                bestStart = start
                bestEnd = end
                minSoFar = end - start
            if s[start] in myTable:
                myTable[s[start]] += 1
                if (myTable[s[start]] > 0):
                    totalElements += 1
            start += 1
            
        if (totalElements == 0 and minSoFar > end - start):
            return s[start:end]
        elif minSoFar <= len(s):
            return s[bestStart:bestEnd]
        else:
            return ""
