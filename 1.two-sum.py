#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target-nums[i]) != i:
                return [i, nums.index(target-nums[i])]

# @lc code=end

print(Solution().twoSum([3,2,4],6))