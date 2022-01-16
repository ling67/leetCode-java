/*
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [5,4,5,1,1,5]
Output: 2
Example 2:


Input: root = [1,4,5,4,4,5]
Output: 2
*/


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
    
    class ResultType {
        int excludeRootMax;     //不包括root的路径的最大值
        int endRootMax;         //严格以root为终节点的路径最大值
        int passRootMax;        //严格通过root的最大路径值，注意不能root为终节点
        private ResultType(int excludeRootMax, int endRootMax, int passRootMax) {
            this.excludeRootMax = excludeRootMax;
            this.endRootMax = endRootMax;
            this.passRootMax = passRootMax;
        }
    }
    
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) {
            return 0;
        }
        ResultType result = help(root);
        return Math.max(Math.max(result.excludeRootMax, result.endRootMax), result.passRootMax) - 1;
    }
    
    ResultType help(TreeNode root) {
        //exit
        if (root == null) {
            return new ResultType(0, 0, 0);
        }
        
        if (root.left == null && root.right == null) {
            return new ResultType(0, 1, 0);   //注意初始化
        }
        
        ResultType result = new ResultType(0, 1, 0);   //注意初始化
        
        //divide
        ResultType left = help(root.left);
        ResultType right = help(root.right);
        
        //conquer
        if (root.left != null) {
            if (root.left.val == root.val) {
                result.endRootMax = left.endRootMax + 1;
                
            }
            result.excludeRootMax = Math.max(Math.max(left.excludeRootMax, left.endRootMax), left.passRootMax);
        }
        
        if (root.right != null) {
            if (root.right.val == root.val) {
                result.endRootMax = Math.max(result.endRootMax, right.endRootMax + 1);
            }
            result.excludeRootMax = Math.max(result.excludeRootMax, Math.max(Math.max(right.excludeRootMax, right.endRootMax), right.passRootMax));
        }
        
        if (root.left != null && root.right != null) {
            if (root.left.val == root.val && root.val == root.right.val) {
                result.passRootMax = left.endRootMax + right.endRootMax + 1;
            }
        }
        return result;
    }
    
}
