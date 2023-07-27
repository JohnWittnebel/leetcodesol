class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # idea: if there are k consecutive 0's, we can place (k-1)/2 flowers in that area
        # we can simply count how many flowers can be planted and see if it is greater than n
        currStringZeros = 0
        totalPlantable = 0
        seenOne = 0

        for ele in flowerbed:
            if ele == 1 and currStringZeros:
                if not seenOne:
                    plantableInArea = currStringZeros // 2
                    seenOne = 1
                else:
                    plantableInArea = (currStringZeros - 1) // 2 
                totalPlantable += plantableInArea
                currStringZeros = 0
            elif ele == 0:
                currStringZeros += 1
            else:
                seenOne = 1
        
        # case for when we ended with a string of 0's
        if currStringZeros:
            if seenOne:
                plantableInArea = currStringZeros // 2 
            else:
                plantableInArea = (currStringZeros + 1) // 2
            totalPlantable += plantableInArea

        return totalPlantable >= n
