class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Strategy:
        # we will halve the size of the smaller array each iteration and do this logn times until
        # the smaller array only has 1-2 elements.

        # To do this, we check the median of nums1 and nums2, WLOG let nums1 be longer. If the
        # median of nums2 > median of nums1 (accessed in O(1) time since arrays are sorted), then we
        # know that the median of the combined arrays is either to the right in nums1 or to the left in
        # nums2. We ignore the n/2 largest values from nums2 and the n/2 smallest values of nums1, and
        # repeat this process with new medians selected from the arrays (minus elements ignored) until 
        # nums2 has a 1-2 elements left.

        # Each iteration will be ignoring n/2 values larger than the median and n/2 values smaller
        # than the median, so when we get to a constant number of values left, the median must remain.

        # Code Start:

        # First, we will make nums1 the longer of the 2 lists
        if len(nums2) > len(nums1):
            swap = nums1
            nums1 = nums2
            nums2 = swap
  
        # We cover some very simple base cases that the recursive algorithm will never reach:


        leftIndex1 = 0
        leftIndex2 = 0
        rightIndex1 = len(nums1) - 1
        rightIndex2 = len(nums2) - 1

        # Very simple base case where |arr2| == |arr1| and they both are size 1, this is so that
        # when we start looking at values around the current median of arr1, we dont go out of bounds
        if ((rightIndex2 - leftIndex2) == 0 and (rightIndex1 - leftIndex1) == 0):
            return float(arr1[leftIndex1] + arr2[leftIndex2]) / 2

        if (len(nums2) == 1):

          # Case where |arr2| == 1, |arr1| is odd
          if (rightIndex1 - leftIndex1) % 2 == 0:
              valToAdd = nums2[0]
              currMedianIndex = (len(nums1) / 2)
              currMedian = nums1[currMedianIndex]
              if valToAdd > currMedian and valToAdd < nums1[currMedianIndex + 1]:
                  return float(currMedian + valToAdd) / 2
              elif valToAdd > currMedian:
                  return float(currMedian + nums1[currMedianIndex + 1]) / 2
              elif valToAdd < currMedian and valToAdd > nums1[currMedianIndex - 1]:
                  return float(currMedian + valToAdd) / 2
              else:
                  return float(currMedian + nums1[currMedianIndex - 1]) / 2

          # Case where |arr2| == 1, |arr1| is even
          if (rightIndex1 - leftIndex1) % 2 == 1:
              valToAdd = nums2[0]
              currMedianIndex = len(nums1) / 2 - 1
              currMedian = nums1[currMedianIndex]
              if valToAdd > currMedian and valToAdd < nums1[currMedianIndex + 1]:
                  return valToAdd
              elif valToAdd > currMedian:
                  return nums1[currMedianIndex + 1]
              else:
                  return currMedian

        # Now we have covered all cases that the recursive cases will not run into
        return float(self.findMedianSortedArraysHelper(nums1, leftIndex1, rightIndex1, nums2, leftIndex2, rightIndex2))

    # Required precon that |arr2| <= |arr1|
    # Required precon that |arr2| >= 2
    def findMedianSortedArraysHelper(self, arr1, leftIndex1, rightIndex1, arr2, leftIndex2, rightIndex2):

        # 2 base cases to consider, based on parity of arr1
        if (rightIndex2 - leftIndex2) == 1:

            valToAdd1 = arr2[leftIndex2]
            valToAdd2 = arr2[rightIndex2]
            currMedianIndex = ((rightIndex1 - leftIndex1) / 2) + leftIndex1
            
            # Case where |arr2| == 2, |arr1| is odd
            if (rightIndex1 - leftIndex1) % 2 == 0:
                currMedian = arr1[currMedianIndex]
                if valToAdd1 >= currMedian and valToAdd1 < arr1[currMedianIndex + 1]:
                    return float(valToAdd1)
                elif valToAdd1 >= currMedian:
                    return float(arr[currMedianIndex + 1])
                elif valToAdd1 < currMedian and valToAdd2 >= currMedian:
                    return float(currMedian)
                elif valToAdd1 < currMedian and valToAdd2 >= arr1[currMedianIndex - 1]:
                    return float(valToAdd2)
                else:
                    return float(arr[currMedianIndex - 1])
  
            # Case where |arr2| == 2, |arr1| is even
            if (rightIndex1 - leftIndex1) % 2 == 1:
                currMedianLeft = arr1[currMedianIndex]
                currMedianRight = arr1[currMedianIndex + 1]
                currSize = rightIndex1 - leftIndex1 + 1
                if valToAdd1 >= currMedianRight and (currSize == 2 or valToAdd1 < arr1[currMedianIndex + 2]):
                    return float(valToAdd1 + currMedianRight) / 2
                elif valToAdd1 >= currMedianRight:
                    return float(currMedianRight + arr1[currMedianIndex + 2]) / 2
                elif valToAdd1 >= currMedianLeft and valToAdd2 <= currMedianRight:
                    return float(valToAdd1 + valToAdd2) / 2
                elif valToAdd1 >= currMedianLeft:
                    return float(valToAdd1 + currMedianRight) / 2
                elif valToAdd2 >= currMedianRight:
                    return float(currMedianLeft + currMedianRight) / 2
                elif valToAdd2 >= currMedianLeft:
                    return float(currMedianLeft + valToAdd2) / 2
                elif currSize == 2 or valToAdd2 > arr1[currMedianIndex - 1]:
                    return float(valToAdd2 + currMedianLeft) / 2
                else:
                    return float(currMedianLeft + arr1[currMedianIndex - 1]) / 2
        
        # Base cases covered, now the recursive case
        arr1MedianIndex = ((rightIndex1 - leftIndex1) / 2) + leftIndex1
        arr1Median = arr1[arr1MedianIndex]
        if (rightIndex1 - leftIndex1) % 2 == 1:
            arr1Median = float(arr1Median + arr1[arr1MedianIndex + 1]) / 2

        arr2MedianIndex = ((rightIndex2 - leftIndex2) / 2) + leftIndex2
        arr2Median = arr2[arr2MedianIndex]
        if (rightIndex2 - leftIndex2) % 2 == 1:
            arr2Median = float(arr2Median + arr2[arr2MedianIndex + 1]) / 2

        if arr1Median < arr2Median:
            if (rightIndex2 - leftIndex2) % 2 == 1:
                return self.findMedianSortedArraysHelper(arr1, leftIndex1 + rightIndex2 - arr2MedianIndex - 1, rightIndex1, arr2, leftIndex2, arr2MedianIndex + 1)
            else:
                return self.findMedianSortedArraysHelper(arr1, leftIndex1 + rightIndex2 - arr2MedianIndex, rightIndex1, arr2, leftIndex2, arr2MedianIndex)
        elif arr1Median > arr2Median:
            return self.findMedianSortedArraysHelper(arr1, leftIndex1, rightIndex1 - arr2MedianIndex + leftIndex2, arr2, arr2MedianIndex, rightIndex2)
        else:
            return arr1Median
                
x = Solution()
print(x.findMedianSortedArrays([1,2,5,6,10,11,15,22], [1,3,4,7,9,11,24,25,26,27,28,29,30]))
#[1,1,2,3,4,5,6,7,9,10,11,15,22,24,25,26,27,28,29,30]

#answer = 10.5

#Iteration 1:
#8 vs 24 

#Iteration 2:
#[6,10,11,15,22] vs [1,3,4,7,9,11,24,25,26,27]
# 11 vs 10

#Iteration 3:
#[6,10,11] vs [4,7,9,11,24,25,26,27]
#10 vs 17.5



print(x.findMedianSortedArrays([1,2],[3,4]))
print("expected: 2.5")

print(x.findMedianSortedArrays([1,2,3,4],[3,4]))
print("expected: 3")

print(x.findMedianSortedArrays([4,5],[1,2]))
print("expected: 3")

print(x.findMedianSortedArrays([5,6,7,8],[1,2]))
print("expected: 5.5")

print(x.findMedianSortedArrays([5,6,7,8],[1,10]))
print("expected: 6.5")

print(x.findMedianSortedArrays([1,2,9,10],[5,6]))
print("expected: 5.5")

print(x.findMedianSortedArrays([1,2,3],[4]))
print("expected: 2.5")

print(x.findMedianSortedArrays([2,3,5,6],[4]))
print("expected: 4")

print(x.findMedianSortedArrays([3],[1,2,4]))
print("expected: 2.5")
