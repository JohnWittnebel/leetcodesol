class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # We will cut the problem into 3 steps:
        # 1. insert the intervals that appear before the newInterval
        # 2. insert any potentially overlapping intervals into the newInterval
        # 3. insert any remaining intervals that appear after newInterval
        outputIntervals = []

        currInd = 0
        while (currInd < len(intervals) and intervals[currInd][1] < newInterval[0]):
            outputIntervals.append(intervals[currInd])
            currInd += 1
        
        # special case where the new interval is completely at the end of the current
        # intervals
        if currInd == len(intervals):
            intervals.append(newInterval)
            return intervals
        
        # now we are at the (potentially) overlapping part
        start = min(intervals[currInd][0], newInterval[0])
        while (currInd < len(intervals) and intervals[currInd][0] <= newInterval[1]):
            currInd += 1
        
        if currInd == 0:
            outputIntervals.append(newInterval)
        # new interval might be the furthest to the right of all intervals, then we get this case
        elif currInd == len(intervals):
            outputIntervals.append([start, max(newInterval[1], intervals[currInd-1][1])])
            return outputIntervals
        else:
            end = max(newInterval[1], intervals[currInd-1][1])
            outputIntervals.append([start, end])

        # now we append any remaining intervals
        while currInd < len(intervals):
            outputIntervals.append(intervals[currInd])
            currInd += 1
        return outputIntervals
