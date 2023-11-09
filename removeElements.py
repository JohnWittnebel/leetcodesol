# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        initHead = head
        prev = head
        head = head.next
        while head and head.next != None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        if head and head.val == val:a
            prev.next = None
        return initHead        

        
