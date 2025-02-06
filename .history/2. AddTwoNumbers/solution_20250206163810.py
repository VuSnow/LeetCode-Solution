"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        result = dummy
        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            # if l1 is not None, plus l1.val to total
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            # if l2 is not None, plus l2.val to total
            if l2 is not None:
                total += l2.val
                l2 = l2.next
            digit = total % 10
            carry = total // 10
            dummy.next = ListNode(digit)
            dummy = dummy.next

        return result.next

# Test case function


def list_to_linked_list(numbers):
    """Convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test cases
solution = Solution()

# Test Case 1
l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print(f"test case 1: {linked_list_to_list(result)}")

# Test Case 2
l1 = list_to_linked_list([0])
l2 = list_to_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print(f"test case 2: {linked_list_to_list(result)}")

# Test Case 3
l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(f"test case 3: {linked_list_to_list(result)}")

# Additional Edge Case: Different Lengths
l1 = list_to_linked_list([1])
l2 = list_to_linked_list([9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Expected Output: [0, 0, 0, 1]

# Additional Edge Case: Carry Over to a New Node
l1 = list_to_linked_list([5])
l2 = list_to_linked_list([5])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Expected Output: [0, 1]
