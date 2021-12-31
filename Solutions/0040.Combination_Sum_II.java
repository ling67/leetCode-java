/*
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
*/


class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<>();
        if (candidates == null || candidates.length == 0) {
            return results;
        }
        //先排序
        Arrays.sort(candidates);    
        help(candidates, 0, new ArrayList<Integer>(), target, results);
        return results;
    }
    
    //
    private void help(int[] nums,
                      int startIndex,
                      List<Integer> combination,
                      int target,
                      List<List<Integer>> results) {
        
        if (target == 0) {
            results.add(new ArrayList<>(combination));
        }
        
        for (int i = startIndex; i < nums.length; i++) {
            if (nums[i] > target) {
                break;
            }
            if (i != startIndex && nums[i] == nums[i-1]) {
                continue;
            } 
            combination.add(nums[i]);
            help(nums, i + 1, combination, target - nums[i], results);
            combination.remove(combination.size() - 1);
        }
        
    }
    
}

