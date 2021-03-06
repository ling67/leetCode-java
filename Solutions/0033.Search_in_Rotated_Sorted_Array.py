/*
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
*/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            #无论哪种情况我们只考虑什么时候l要向中间移动
            elif nums[l] <= nums[m] < target or target < nums[l] <= nums[m] or nums[m] < target < nums[l]:   
                l = m
            else:
                r = m
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[0] <= nums[mid] < target:
                    start = mid
                else:
                    end = mid
            else:
                if target <= nums[mid] <= nums[-1]:
                    end = mid
                else:
                    start = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
    
        return -1
            
/*************************************java version*****************************************/

class Solution {
    public int search(int[] nums, int target) {
        
        if(nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0, end = nums.length - 1;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return mid;
            } 
            
            if (nums[start] < nums[mid]) {
                if ( nums[start] <= target && target <= nums[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else {
                if ( nums[mid] <= target && target <= nums[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            } 
        }
        
        if (nums[start] == target) {
            return start;
        }
        
        if (nums[end] == target) {
            return end;
        }
        return -1;
    }
}
