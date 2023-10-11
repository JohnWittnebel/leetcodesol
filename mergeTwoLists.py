# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val < list2.val:
            sortedHead = list1
            list1 = list1.next
        else:
            sortedHead = list2
            list2 = list2.next

        currPoint = sortedHead
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                currPoint.next = list1
                list1 = list1.next
            else:
                currPoint.next = list2
                list2 = list2.next
            currPoint = currPoint.next
        
        if list1 == None:
            currPoint.next = list2
        else:
            currPoint.next = list1
        return sortedHead
