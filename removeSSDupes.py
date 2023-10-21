# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = head
        newHead = prev
        startOfNew = head
        endOfNew = head.next
        while (endOfNew != None):
            isDupe = False
            while (startOfNew.val == endOfNew.val) and endOfNew != None:
                isDupe = True
                endOfNew = endOfNew.next
            if isDupe:
                if newHead == prev:
                    newHead = endOfNew
                prev.next = endOfNew
                startOfNew = endOfNew
                if endOfNew != None:
                    endOfNew = endOfNew.next
            else:
                prev = prev.next
                startOfNew = endOfNew
                if endOfNew != None:
                    endOfNew = endOfNew.next
        return newHead

X = Solution()
print(X.deleteDuplicates([1,2,2,3,3,4,5]))
