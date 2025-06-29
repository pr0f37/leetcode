"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            idx = self.binary_search(nums1, i)
            nums1.insert(idx, i)
        return (
            nums1[len(nums1) // 2]
            if len(nums1) % 2 == 1
            else (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        )

    def binary_search(self, nums: list[int], x: int) -> int:
        """Binary search to find the index of x in nums."""
        left, right = 0, len(nums) - 1
        while left <= right:
            idx = (left + right) // 2
            if nums[idx] == x:
                return idx + 1
            elif nums[idx] > x:
                right = idx - 1
            else:
                left = idx + 1
        return left
