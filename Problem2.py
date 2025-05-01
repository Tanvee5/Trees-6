# Problem 2 : Serialize and Deserialize Binary Tree
# Time Complexity : O(N) where N is the number of nodes
# Space Complexity : O(N) where N is the number of nodes
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # edge case if root node is None then return "# "
        if not root:
            return "# "
        # define sb variable to store the value of the node
        sb = []
        # defint the queue to store the node while traversing in bfs manner
        q = deque()
        # add root to the queue
        q.append(root)
        # loop till the queue is not empty
        while q:
            # pop the top element from the queue
            currNode = q.popleft()
            # check if the node is not None then append the value of the node to the sb and add left and right node to the queue
            if currNode:
                sb.append(str(currNode.val))
                q.append(currNode.left)
                q.append(currNode.right)
            else:
                # else add '#' to the sb
                sb.append("#")
            # append " " to the sb to mark as end of the string
            sb.append(" ")
        # return the sb as string 
        return ''.join(sb)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # convert the data to array
        strArr = data.split()
        # check if the strArr is None or the first letter is # then return None
        if not strArr or strArr[0] == "#":
            return None
        # define variable i is 0
        i = 0
        # create a TreeNode for the int for strArr[i]
        root = TreeNode(int(strArr[i]))
        # increment the i pointer
        i += 1
        # define queue
        q = deque()
        # append root to queue
        q.append(root)
        # loop till queue is not Empty and i is less than length of the strArr
        while q and i < len(strArr):
            # pop the top element from the queue
            currNode = q.popleft()
            # check if the character of strArr at i position is not equal to # and if it is then create TreeNode for the character and add as left child
            if strArr[i] != "#":
                currNode.left = TreeNode(int(strArr[i]))
                # append the left node of current node to queue
                q.append(currNode.left)
            # increment i
            i += 1
            # check if i is less than length of the strArr and character of strArr at i position is not equal to # and if it is then create TreeNode for the character and add as right child
            if i < len(strArr) and strArr[i] != "#":
                currNode.right = TreeNode(int(strArr[i]))
                # append the right node of current node to queue
                q.append(currNode.right)
            # increment i
            i += 1
        # return root
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))