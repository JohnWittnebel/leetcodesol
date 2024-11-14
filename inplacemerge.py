class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        currIndex1 = 0
        currIndex2 = 0
        for i in reversed(range(m)):
            nums1[i+n] = nums1[i]
        
        for i in range(m+n):
            if currIndex1 == m:
                nums1[i] = nums2[currIndex2]
                currIndex2 += 1
            elif currIndex2 == n:
                nums1[i] = nums1[currIndex1+n]
                currIndex1 += 1
            elif nums1[currIndex1+n] > nums2[currIndex2]:
                nums1[i] = nums2[currIndex2]
                currIndex2 += 1
            else:
                nums1[i] = nums1[currIndex1+n]
                currIndex1 += 1


                
        
