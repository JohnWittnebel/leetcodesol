class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        # Strategy: We can do this in O(n^2) time by checking if we can create 3 equal parts
        #           with the first k digits, for k=1 to n.
    
        totalLen = len(arr)
        for i in range(totalLen):
            # i is the length of the first block that we will attempt to match the rest of the string to
            # you may think this can be <= n/3, but we could have [0,0,0,0,0,1,1,1] e.g.
            firstBlock = self.removeLeadingZeroes(arr[0:i])
            
            # now numberToMatch does not have leading 0's, we will break the leading 0's from 
            # the second block and see if it is the same, and then the third block
            secondBlock = self.removeLeadingZeroes(arr[i:])

            if secondBlock[0:len(firstBlock)] == firstBlock:
                # Look to see if there is an equal third block
                thirdBlock = self.removeLeadingZeroes(secondBlock[len(firstBlock):])
                if (thirdBlock == firstBlock):
                    # we have a valid answer, but we need to know how many leading 0's secondBlock had
                    count1 = 0
                    count2 = 0
                    currIndex = i
                    for elem in arr[i:]:
                        if elem == 0:
                          count2 += 1
                        else:
                          break
                    for elem in arr:
                        if elem == 0:
                            count1 += 1
                        else:
                            break
                    return [i-1,i+i+count2-count1]
        return [-1,-1]


    def removeLeadingZeroes(self, arr):
        currIndex = 0
        if len(arr) == 0:
            return arr
        while (currIndex < len(arr)) and (arr[currIndex] == 0):
            currIndex += 1
        return arr[currIndex:]

x = Solution()
print(x.threeEqualParts([0,0,0,0,1,0,1,1]))
