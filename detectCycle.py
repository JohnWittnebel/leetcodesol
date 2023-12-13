# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # idea: this is a classic problem. The solution is to use two pointers, one that
        #.      moves 2 at a time and another that moves 1 at a time. If the pointers are
        #       ever at the same node, then there is a cycle.
        #       Once we have detected that there is a cycle, we can continue until pointer1 and
        #       pointer2 are at the same position again, at that point pointer1 will have done a full cycle
        #       Now that we know the cycle length, we can start from the head again find the first 
        #       first position where after cycle length the node is the same.
        pointer1 = head
        if pointer1 == None:
            return None

        pointer2 = head.next
        if pointer2 == None:
            return None
        
        while pointer2 != pointer1:
            if pointer2.next == None or pointer2.next.next == None:
                return None
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next
        
        cycleLen = 1
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        while pointer2 != pointer1:
            if pointer2.next == None or pointer2.next.next == None:
                return -1
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next
            cycleLen += 1
        
        cycleLenCheck = head
        currInd = 0
        cycleArr = []
        for _ in range(cycleLen):
            cycleArr.append(0)
        
        while cycleLenCheck != cycleArr[currInd % cycleLen]:
            cycleArr[currInd % cycleLen] = cycleLenCheck
            cycleLenCheck = cycleLenCheck.next
            currInd += 1
        return cycleLenCheck

        
