'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        curr_row = [1]
        for i in range(0, numRows):
            pascal_triangle.append(curr_row)
            t1 = curr_row[:]
            t1.append(0)
            t2 = curr_row[:]
            t2.insert(0, 0)
            curr_row = [t1[j] + t2[j] for j in range(len(t1))]
        return pascal_triangle