"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None

        myQueue = []
        myQueue.append([root,1])
        while myQueue:
            currEle = myQueue.pop(0)
            depth = currEle[1]
            currNode = currEle[0]
            if currNode.left:
                myQueue.append([currNode.left, depth+1])
            if currNode.right:
                myQueue.append([currNode.right, depth+1])
            if len(myQueue) > 0 and myQueue[0][1] == depth:
                currNode.next = myQueue[0][0]
            else:
                currNode.next = None
        return root
