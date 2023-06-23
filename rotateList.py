# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Idea: if we find the kth node from the end we put that at the start. if k >= len(list), then
        #.      we set k to k % len(list), since if we are rotating len(list) times we get
        #       the original list back

        lenList = 1
        start = head
        if (head == None):
            return None
        while (head.next != None):
            lenList += 1
            head = head.next
        
        head = start
        valFromEnd = k % lenList
        if valFromEnd == 0:
            return head

        currInd = 1
        while lenList - currInd != valFromEnd:
            head = head.next
            currInd += 1
        newStart = head.next
        head.next = None
        newHead = newStart
        while newHead.next != None:
            newHead = newHead.next
        newHead.next = start
        return newStart
