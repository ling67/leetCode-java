/*
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.help(root.left, root.right)
        
    def help(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:   
        #exit
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        #devide
        return self.help(left.left, right.right) and self.help(left.right, right.left)
        
        

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return help(root.left, root.right);
    }
    
    //1.check 2 tree is mirror
    private boolean help(TreeNode left, TreeNode right) {
        //3.
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        if (left.val != right.val) {
            return false;
        }
        //2.conquer & deivide
        return help(left.left, right.right) && help(left.right, right.left); 
    }
    
}
