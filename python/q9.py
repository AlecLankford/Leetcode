"""
ACCEPTED
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true
"""
class Solution:
    def isPalindrome(self, x:int) -> bool:
        y = str(x)[::-1]
        if str(x) == y:
            return True
        else:
            return False