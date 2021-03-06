"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

"""
思路：
递归：经过这个点最大的路径和是多少，遍历整个树，比较经过每个点的路径的和，最后得到肯定是最大的
递归的时候我们需要什么：我们需要以左子树结尾的最大的路径是多少，右子树结尾的最大的路径是多少
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        self.helper(root)
        return self.max_sum
        
    #return max sum end with root    
    def helper(self, root):
        if not root:
            return 0
        l = max(0, self.helper(root.left))
        r = max(0, self.helper(root.right))
        self.max_sum = max(self.max_sum, root.val + l + r)
        return root.val + max(l, r)
