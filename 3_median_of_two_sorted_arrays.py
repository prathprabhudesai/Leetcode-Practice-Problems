'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Follow up: The overall run time complexity should be O(log (m+n)).
'''
# brute force would be - add two arrays in sorted manner and find median
# for that we have to create an array with len(nums1) + len(nums2)
# and do the merge process we do in merge sort
# since both arrays are sorted we can make use of that property
# some modified sort of binary search may be a good place to start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        # find the smaller array and find the X partition, then we can find the Y partition
        # such that, all the left side will have lower values than the right side
        if (n1 < n2):
            x, y = nums1, nums2
        else:
            x, y = nums2, nums1
        start_x, end_x = 0, len(x)
        median = 0
        while start_x <= end_x:
            part_x = int((start_x + end_x) / 2)
            part_y = int((n1 + n2 + 1) / 2) - part_x

            max_left_x = float('-inf') if part_x == 0 else x[part_x - 1]
            min_right_x = float('inf') if part_x == len(x) else x[part_x]

            max_left_y = float('-inf') if part_y == 0 else y[part_y - 1]
            min_right_y = float('inf') if part_y == len(y) else y[part_y]

            if (max_left_x <= min_right_y) and (max_left_y <= min_right_x):
                # we found the right partition:
                if (n1 + n2) % 2 == 0:
                    median = (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    median = max(max_left_x, max_left_y)
                break
            elif max_left_x > min_right_y:
                end_x = part_x - 1
            else:
                start_x = part_x + 1
        return median

