#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        output = 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        while index < len(s):
            print(f"I Value: {index}")
            if index == len(s)-1: # Last number in string
                output += roman_dict.get(s[index])
                index += 1
            elif roman_dict.get(s[index+1]) > roman_dict.get(s[index]):
                # Minus the next number
                output += (roman_dict.get(s[index+1]) - roman_dict.get(s[index]))
                print("Minusing number")
                print(f"Value: {roman_dict.get(s[index+1]) - roman_dict.get(s[index])}")
                # Add a counter to i
                index += 2
            else:
                # Add the number
                output += roman_dict.get(s[index])
                print(f"Value: {roman_dict.get(s[index])}")
                index += 1
        return output
            
# @lc code=end

