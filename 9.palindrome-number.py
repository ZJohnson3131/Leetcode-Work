#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        for i in range(len(str_int)):
            if str_int[i] == str_int[-(i+1)]:
                continue
            else:
                return False
            
        else:
            return True

# @lc code=end

