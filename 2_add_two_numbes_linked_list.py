'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addNode(self, lsum, ltail, value):
        if lsum is None:
            lsum = ListNode(value)
            ltail = lsum
        else:
            temp = ListNode(value)
            ltail.next = temp
            ltail = temp
        return lsum, ltail

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        lsum, ltail = None, None
        currsum, carry = 0, 0
        while carry or l1 or l2:
            currsum = carry
            if l1:
                currsum += l1.val
                l1 = l1.next
            if l2:
                currsum += l2.val
                l2 = l2.next
            if currsum >= 10:
                carry = 1
                currsum = currsum - 10
            else:
                carry = 0
            lsum, ltail = self.addNode(lsum, ltail, currsum)
        return lsum