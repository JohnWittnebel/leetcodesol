class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Strat: The brute-force check is O(n^3).
        #        Alternative: sort the array. After that, we can fix any particular element and
        #                     solve the 2SUM problem on the remainder of the array in O(n) time.
        #                     This results in O(n^2) total time.

        sortedArr = sorted(nums)
        retArr = []
        
        if len(sortedArr) < 3:
            return []

        for i in range(len(sortedArr)):
            retArr += self.twoSum(sortedArr[0:i] + sortedArr[i+1:], -sortedArr[i])
        if len(retArr) > 0:
            print(retArr)
            return self.removeDuplicates(sorted(retArr))
        else:
            return []
    
    def removeDuplicates(self, arr):
        retArr = []
        initialLen = len(arr)
        for i in range(initialLen - 1):
            if arr[i] != arr[i+1]:
                retArr += [arr[i]]
        if len(retArr) > 0:
            if retArr[len(retArr) - 1] != arr[initialLen - 1]:
                retArr += [arr[initialLen - 1]]
                return retArr
        else:
            return [arr[initialLen - 1]]
    
    # Prereq: nums is already sorted
    def twoSum(self, nums, target):
        leftIndex = 0
        rightIndex = len(nums) - 1
        retArr = []
        while (leftIndex != rightIndex):
            if (nums[leftIndex] + nums[rightIndex] > target):
                rightIndex -= 1
            elif (nums[leftIndex] + nums[rightIndex] < target):
                leftIndex += 1
            else:
                retArr += [sorted([nums[leftIndex],nums[rightIndex],-target])]
                leftIndex += 1
        print(retArr)
        return retArr
        

x = Solution()
print(x.threeSum([-1,0,1,2,-1,-4]))

