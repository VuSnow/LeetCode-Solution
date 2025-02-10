"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right_ptr = max_length = 0
        char_set = []

        for left_ptr in range(len(s)):
            if (s[left_ptr] not in char_set):
                char_set.append(s[left_ptr])
                max_length = max(max_length, left_ptr - right_ptr + 1)
            else:
                while (s[left_ptr] in char_set):
                    char_set.remove(s[right_ptr])
                    right_ptr += 1

        return max_length
