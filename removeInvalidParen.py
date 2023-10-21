class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Idea: As we scan, as soon as we reach a mismatch "eg. ()(()))", we must remove
        #       one of the closing parentheses. At the end if we have too many open parentheses
        #       we also need to remove some opening ones.

        solnSet = []
        openParen = 0
        partialSoln = ""
        closeIndices = []
        currInd = 0
        startInd = 0
        for char in s:
            if char == "(":
                openParen += 1
                partialSoln += char
                currInd += 1
            elif char != ")":
                partialSoln += char
                currInd += 1
            elif openParen > 0:
                closeIndices.append(currInd)
                openParen -= 1
                partialSoln += char
                currInd += 1
            else:
                # this is the case where we actually have to subdivide our cases
                closeIndices.append(currInd)
                partialSoln += ")"
                newSolns = []
                newPartials = []
                for ele in closeIndices:
                    newPartials.append(partialSoln[startInd:ele] + partialSoln[ele+1:])
                if (len(solnSet) > 0):
                    for prefix in solnSet:
                        for suffix in newPartials:
                            newSolns.append(prefix + suffix)
                else:
                    newSolns = newPartials
                solnSet = self.removeDupes(newSolns)
                partialSoln = ""
                currInd += 1
                startInd = currInd
                closeIndices = []
                openParen = 0
        # All that is left is the final partial soln, if it is balanced we are done
        # Otherwise, we have to remove the open parentheses from the partialSoln
        if (openParen == 0):
            if (len(solnSet) == 0):
                solnSet = [partialSoln]
            else:
                i = 0
                for i in range(len(solnSet)):
                    solnSet[i] += partialSoln
        else:
            revPartial = ""
            for char in partialSoln:
                if char == "(":
                    revPartial += ")"
                elif char == ")":
                    revPartial += "("
                else:
                    revPartial += char
            suffixes = self.removeInvalidParentheses(revPartial[::-1])
            
            trueSuffixes = []
            for suffix in suffixes:
                trueSuffixes.append(suffix[::-1])
            newSolnSet = []
            if (len(solnSet) == 0):
                newSolnSet = trueSuffixes
            else:
                for prefix in solnSet:
                    for suffix in trueSuffixes:
                        newSolnSet.append(prefix + suffix)
            solnSet = self.removeDupes(newSolnSet)

        if (len(solnSet) == 0):
            return [""]
        return solnSet

    # Remove duplicates in an array
    def removeDupes(self, arr):
        arr.sort()
        retVal = []
        if len(arr) <= 1:
            return arr
        prev = arr[0]
        retVal.append(prev)
        currInd = 1
        while currInd <= len(arr) - 1:
            if prev != arr[currInd]:
                prev = arr[currInd]
                retVal.append(prev)
            currInd += 1
        return retVal

                
x = Solution()
print(x.removeInvalidParentheses("(()"))
