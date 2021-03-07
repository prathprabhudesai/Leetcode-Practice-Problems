'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Voting Algorithm
        # it's a two step process
        # first you have to find a candidate for majority element
        # then verify if the majority element return is in fact the majority element
        # but according to the problem statement, you can assume that majority element always
        # exists in the array, we don't have to do the next step of verification
        majority_index, count = 0, 1
        for i in range(len(nums)):
            if nums[majority_index] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority_index = i
                count = 1
        return nums[majority_index]