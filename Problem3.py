# Problem 3 : Binary Tree Vertical Order Traversal
# Time Complexity : O(N) where N is the total number of nodes in a binary tree
# Space Complexity : O(N) where N is the total number of nodes in a binary tree
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

from collections import deque, defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case if the root node is None ie emoty tree then return empty list
        if root is None: 
            return []
        
        # define result list variable which stores the list of the node for the particular column
        result = []
        # define deque and append root node. This queue will store the node of the tree.
        q = deque([root])
        # define deque and append the column number for the root node. This queue will store the column number for particular node.
        colq = deque([0])
        # define hash map which will store column number as key and list of nodes that belong to the column as value
        columnTable = defaultdict(list)
        # define min and max variable which will store the minimum and maximum column number
        minCol = 0
        maxCol = 0
        # loop through q queue
        while q: 
            # get the top node and top column number from both queues
            currNode = q.popleft()
            currCol = colq.popleft()
            # add the current node to the list to the current column key in the hash map
            columnTable[currCol].append(currNode.val)
            
            # check if the left of the current node is not none then append the left node and column number (column number of root - 1) to the queues
            if currNode.left:
                q.append(currNode.left)
                colq.append(currCol - 1)
                # get the minimum column number as minimum between minimum column number and column number of the left node
                minCol = min(minCol, currCol - 1)
            # check if the right of the current node is not none then append the right node and column number (column number of root + 1) to the queues
            if currNode.right:
                q.append(currNode.right)
                colq.append(currCol + 1)
                # get the maximum column number as maximum between maximum column number and column number of the right node
                maxCol = max(maxCol, currCol + 1)
        # loop from minimum column number to maximum column number
        for col in range(minCol, maxCol+1):
            # append the list of that particular column in the result
            result.append(columnTable[col])
        # return result
        return result