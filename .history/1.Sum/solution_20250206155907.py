"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for index in range(len(nums)):
            remaining = target - nums[index]
            new_list = nums[index+1:]
            if remaining in new_list:
                output.extend([index, new_list.index(remaining) + index + 1])
                return output  # this return statement to stop execution when the first valid pair is found
        return output


solution = Solution()
# Test case 1
nums1 = [2, 7, 11, 15]
target1 = 9
# Output: [0, 1]
print(f"test case 1: {solution.twoSum(nums1, target1)}")

# Test case 2
nums2 = [3, 2, 4]
target2 = 6
print(f"test case 2: {solution.twoSum(nums2, target2)}")  # Output: [1, 2]

# Test case 3
nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
