class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # idea: We can do this in O(n^2) time by giving 1 candy to the lowest rated kids,
        #       and each subsequent loop giving 1 to the lowest rated kids if possible, or 
        #       the minimum if they are next to someone who was already given candy.
        #.      To be a bit more clever, we can attempt to find monotonically increasing and 
        #.      decreasing sequences in the ratings, and assign candies based on the length of 
        #       these sequences. There can be issues where a peak is the end of a monotonically
        #.      increasing sequence of length 3 but the start of a monotonically decreasing
        #       sequence of length 4, and that child would need to receive 4 candies, so we must be a little careful.

        increasingDistance = [1]
        decreasingDistance = [1]
        index = 1
        while index < len(ratings):
            if ratings[index-1] < ratings[index]:
                increasingDistance.append(increasingDistance[index-1] + 1)
            else:
                increasingDistance.append(1)
            decreasingDistance.append(1)
            index += 1
        
        index = len(ratings)-2
        while index >= 0:
            if ratings[index+1] < ratings[index]:
                decreasingDistance[index] = decreasingDistance[index+1] + 1
            else:
                decreasingDistance[index] = 1
            index -= 1
        
        numCandies = 0
        for ind in range(len(ratings)):
            numCandies += max(decreasingDistance[ind], increasingDistance[ind])
        return numCandies
