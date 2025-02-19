'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palin_sub = []
        longest_palindrome = ""
        for index in range(1, len(s) - 1):
            left = index - 1
            right = index + 1
            while left >= 0 and right <= len(s) - 1:
                if (s[left] != s[right]):
                    break
                palin_sub.append(s[left:(right + 1)])
                left = left - 1
                right = right + 1

        if palin_sub:
            longest_palindrome = max(
                palin_sub, key=lambda substring: len(substring))
            print(longest_palindrome)
        else:
            print("No palindromic substring found.")
        return palin_sub


print(Solution().longestPalindrome("babad"))
