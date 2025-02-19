'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''


class solution(object):
    def reverse(self, x):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        if x == 0 or x == 1:
            return x
        reversed = 0
        num = abs(x)
        is_negative = x < 0

        while num > 0:
            digit = num % 10
            reversed = reversed * 10 + digit
            num /= 10

        if reversed > INT_MAX:
            return 0
        return -reversed if is_negative else reversed
