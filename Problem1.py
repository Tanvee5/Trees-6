# Problem 1 : Range Sum of BST
# Time Complexity : 
'''
Brute Force - O(n) where n is the number of nodes in the Tree
int based recursion - O(n) where n is the number of nodes in the Tree
conditional void recursion - O(n) where n is the number of nodes in the Tree
condition int recursion - O(n) where n is the number of nodes in the Tree
'''
# Space Complexity : 
'''
Brute Force - O(n) where n is the number of nodes in the Tree
int based recursion - O(n) where n is the number of nodes in the Tree
conditional void recursion - O(h) where h is height of the tree
conditional int based recursion - O(h) where h is height of the tree
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Brute Force Recursive
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # sum variable to store the sum of the numbers which are in range from lwo to high
        sum = 0
        # void helper recvursive function to calculate the sum
        def helper(root: Optional[TreeNode], low: int, high: int) -> None:
            # sum is the global variable
            nonlocal sum
            # base case if the root node is none then return none 
            if root == None: return None
            # logic
            # check if the value of the root node is between range and if it is then add the value to the sum 
            if root.val >= low and root.val <= high:
                sum += root.val
            # call recursiverly the funtion with the left child of root node
            helper(root.left, low, high)
            # call recursiverly the funtion with the right child of root node
            helper(root.right, low, high)
        # call the helper funtion with the root node
        helper(root, low, high)
        # return the sum as a result
        return sum

# int based recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # int helper recvursive function to calculate the sum
        def helper(root: Optional[TreeNode], low: int, high: int) -> int:
            # base case if the root node is None then return 0
            if root == None: return 0
            # logic
            # define local sum variable to store the sum of the numbers
            sum = 0
            # check if the value of the root node is between range and if it is then add the value to the sum
            if root.val >= low and root.val <= high:
                sum += root.val
            # call recursiverly the funtion with the left child of root node and store the value of sum in the left variable
            left = helper(root.left, low, high)
            # call recursiverly the funtion with the right child of root node and store the value of sum in the right variable
            right = helper(root.right, low, high)
            # return the sum of left, right and sum variable
            return left + right + sum
        # call helper function with parameter root node, low and high and return the value
        return helper(root, low, high)

# conditional void recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # sum variable to store the sum of the numbers which are in range from lwo to high
        sum = 0
        # void helper recvursive function to calculate the sum conditionally
        def helper(root: Optional[TreeNode], low: int, high: int) -> None:
            # sum is the global variable
            nonlocal sum
            # base case if the root node is none then return none 
            if root == None: return
            # logic
            # check if the value of the root node is between range and if it is then add the value to the sum 
            if root.val >= low and root.val <= high:
                sum += root.val
            # check if the value of root is less than or equal to low then only call recursively helper function with left child of the root node
            if root.val >= low:
                helper(root.left, low, high)
            # check if the value of root is greater than or equal to high then only call recursively helper function with right child of the root node
            if root.val <= high:
                helper(root.right, low, high)
        # call the helper funtion with the root node
        helper(root, low, high)
        # return the sum as a result
        return sum

# conditional int based recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # int helper recvursive function to calculate the sum
        def helper(root: Optional[TreeNode], low: int, high: int) -> int:
            # base case if the root node is None then return 0 
            if root == None: return 0
            # logic
            # define local sum variable to store the sum of the numbers
            sum = 0
            # check if the value of the root node is between range and if it is then add the value to the sum
            if root.val >= low and root.val <= high:
                sum += root.val
            # check if the value of root is less than or equal to low then only call recursively helper function with left child of the root node and add value to sum
            if root.val >= low:
                sum += helper(root.left, low, high)
            # check if the value of root is greater than or equal to high then only call recursively helper function with right child of the root node and add value to sum
            if root.val <= high:
                sum +=  helper(root.right, low, high)
            # return the sum
            return sum
        # call helper function with parameter root node, low and high and return the value
        return helper(root, low, high)