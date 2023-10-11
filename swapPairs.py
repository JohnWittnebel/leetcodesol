# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
        temp = head.next
        newHead = temp
        head.next = self.swapPairs(temp.next)
        temp.next = head

        return newHead
