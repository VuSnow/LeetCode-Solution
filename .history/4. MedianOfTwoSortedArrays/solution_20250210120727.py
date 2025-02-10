'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.The overall run time complexity should be O(log (m+n))

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


class solution(object):
    def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = num1 + num2
        merged.sort()
        total = len(merged)

        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0

    def findMedianSortedArraysSolution2(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(num1)
        n = len(num2)
        if m < n:
            return self.findMedianSortedArraysSolution2(num2, num1)

        merged = []

        # by default len(num1) >= len(num2)
        ptr1 = ptr2 = 0
        while ptr2 < len(num2) and ptr1 < len(num1):
            if num1[ptr1] < num2[ptr2]:
                merged.append(num1[ptr1])
                ptr1 += 1
            else:
                merged.append(num2[ptr2])
                ptr2 += 1

        while ptr1 < len(num1):
            merged.append(num1[ptr1])
            ptr1 += 1

        while ptr2 < len(num2):
            merged.append(num2[ptr2])


array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]
Solution = solution()
Solution.findMedianSortedArraysSolution2(array1, array2)
