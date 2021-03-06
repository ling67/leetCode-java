"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""
"""
与House robber I 相比，这个题目的房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：
1. 房子1没偷：问题变成了对房子2~N做House robber I的问题
2. 房子N没偷：问题变成了对房子1~N-1做House robber I的问题
"""
"""
we can divide the question to two subquestion
robber donot steal first hourse
robber steal first hourse and not steal last hourse
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        max1 = self.subRob(nums[:n-1])
        max2 = self.subRob(nums[1:n])
        return max(max1, max2)
        
    def subRob(self, nums):
        n = len(nums)
        dp_steal = [0] * n
        dp_not_steal = [0] * n
        dp_steal[0], dp_steal[1] = nums[0], nums[1]
        dp_not_steal[0], dp_not_steal[1] = 0, nums[0]
        
        for i in range(2, n):
            dp_steal[i] = dp_not_steal[i-1] + nums[i]
            dp_not_steal[i] = max(dp_steal[i-1], dp_not_steal[i-1])
        return max(dp_steal[n-1], dp_not_steal[n-1])
            
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        not_rob_the_first_house = self.rob1(nums[1:])
        not_rob_the_last_house = self.rob1(nums[:-1])
        
        return max(not_rob_the_first_house, not_rob_the_last_house)
    
    def rob1(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
      
      
#version2 优化

"""
与House robber I 相比，这个题目的房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：
1. 房子1没偷：问题变成了对房子2~N做House robber I的问题
2. 房子N没偷：问题变成了对房子1~N-1做House robber I的问题
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        not_rob_the_first_house = self.rob1(nums[1:])
        not_rob_the_last_house = self.rob1(nums[:-1])
        
        return max(not_rob_the_first_house, not_rob_the_last_house)
    
    def rob1(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        prevMax = nums[0]   #dp[i-2]的最大值
        currMax = max(nums[0], nums[1])   #dp[i-1]的最大值
        
        for i in range(2, len(nums)):
            temp = currMax
            currMax = max(prevMax + nums[i], currMax)
            prevMax = temp
        
        return currMax

 #version3 滚动数组优化
 class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.getMoney(nums[:n-1]), self.getMoney(nums[1:]))
        
    def getMoney(self, array):
        if len(array) == 1:
            return array[0]
        
        dp = [0] * 2
        dp[1] = array[0]
        
        for i in range(2, len(array) + 1):
            dp[i%2] = max(array[i-1] + dp[(i-2)%2], dp[(i-1)%2])
        return max(dp)
 
 
 
 
