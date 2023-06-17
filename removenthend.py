# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listLen = self.getLen(head)
        indexToRemove = listLen - n
        curr = head
        if indexToRemove == 0:
            return head.next
        elif indexToRemove == 1:
            head.next = head.next.next
            return head

        while (indexToRemove > 1):
            curr = curr.next
            indexToRemove -= 1
        curr.next = curr.next.next

        return head
    
    def getLen(self, head):
        if head.next == None:
            return 1
        else:
            return 1 + self.getLen(head.next)
