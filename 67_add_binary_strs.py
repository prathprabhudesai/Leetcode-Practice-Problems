'''
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

for two:
a b     s c
0 0     0 0
0 1     1 0
1 0     1 0
1 1     0 1
sum = xor(a,b)
carry = and(a,b)

for three:
a b c   s c
0 0 0   0 0
0 0 1   1 0
0 1 0   1 0
0 1 1   0 1
1 0 0   1 0
1 0 1   0 1
1 1 0   0 1
1 1 1   1 1
sum = xor(xor(a,b),c)
carry = or(and(a,b), and(xor(a,b), c))
'''

# this is using the image
class Solution:
    def getValueCarry(self, val):
        if (val > 1):
            return val - 2, 1
        else:
            return val, 0

    def addRemaining(self, s, ind, carry, ans):
        val = 0
        while(carry == 1 and ind > -1):
                val = int(s[ind]) + carry
                val, carry = self.getValueCarry(val)
                ans = str(val) + ans
                ind = ind - 1
        ans = s[0:ind+1] + ans
        return ans, carry

    def addBinary(self, a: str, b: str) -> str:
        la = len(a) - 1
        lb = len(b) - 1
        if la == -1: return b
        if lb == -1: return a
        ans = ""
        carry = 0
        while (la != -1) and (lb != -1):
            val = int(a[la]) + int(b[lb]) + carry
            val, carry = self.getValueCarry(val)
            ans = str(val) + ans
            la = la - 1
            lb = lb - 1
        if (la > -1):
            ans, carry  = self.addRemaining(a, la, carry, ans)
        elif (lb > -1):
            ans, carry = self.addRemaining(b, lb, carry, ans)
        if carry:
            ans = "1" + ans
        return ans

# this is using the logical gates
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        if (la - lb) > 0:
            # la is bigger
            b = "0"*(la - lb) + b
            l = la - 1
        else:
            # lb is bigger
            a = "0"*(lb - la) + a
            l = lb - 1
        ans = ""
        carry = 0
        while l > -1:
            x = int(a[l])
            y = int(b[l])
            val = (x^y)^carry
            carry = ((x&y)|((x^y)&carry))
            ans = str(val) + ans
            l = l -1
        if carry:
            ans = "1" + ans
        return ans