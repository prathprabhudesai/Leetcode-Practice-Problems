'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        n = len(height)
        max_water = 0
        for i in range(0, n):
            for j in range(i+1, n):
                curr_val = min(height[i], height[j])*(j - i)
                if max_water < curr_val:
                    max_water = curr_val
        return max_water
        '''
        #optimal solution
        i, j = 0, len(height) - 1
        curr_water, max_water = 0, 0
        while i != j:
            if height[i] >= height[j]:
                curr_water = height[j]*(j-i)
                j -= 1
            else:
                curr_water = height[i]*(j-i)
                i += 1
            if curr_water > max_water:
                max_water = curr_water
        return max_water