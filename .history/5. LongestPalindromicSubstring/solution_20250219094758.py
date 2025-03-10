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
        if not s:
            return ""

        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(
                s, left=i, right=i)       # odd-length palindrome
            len2 = self.expandAroundCenter(
                s, left=i, right=i + 1)     # even-length palindrome
            max_len = max(len1, len2)
            if max_len > end - start:
                # Update start and end indices based on the current center and max length.
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        # Expand the window as long as the characters on both sides match.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome


print(Solution().longestPalindrome("cbbd"))
