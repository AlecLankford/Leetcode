"""
NOT ACCEPTED
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = digits[len(digits)-1] + 1
        y = str(x)
        if len(y) > 1:
            xy = int(y[0])
            xz = int(y[1])
            digits[len(digits)-1] = xy
            digits.append(xz)
            return digits
        else:
            digits[len(digits)-1] = x
            return digits