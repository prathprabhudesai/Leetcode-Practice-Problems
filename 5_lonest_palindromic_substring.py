'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Approach: The time complexity can be reduced by storing results of sub-problems. The idea                   is similar to this post.

        Maintain a boolean table[n][n] that is filled in bottom up manner.
        The value of table[i][j] is true, if the substring is palindrome, otherwise false.
        To calculate table[i][j], check the value of table[i+1][j-1], if the value is true and
        str[i] is same as str[j], then we make table[i][j] true.
        Otherwise, the value of table[i][j] is made false.
        We have to fill table previously for substring of length = 1 and length =2 because
        as we are finding , if table[i+1][j-1] is true or false , so in case of
        (i) length == 1 , lets say i=2 , j=2 and i+1,j-1 doesn’t lies between [i , j]
        (ii) length == 2 ,lets say i=2 , j=3 and i+1,j-1 again doesn’t lies between [i , j].

        '''
        # length of string
        n = len(s)

        # create a table
        table = [[False for x in range(n)] for y in range(n)]

        # all substrings of length 1 are palindrome
        max_length = 1
        for i in range(0, n):
            table[i][i] = True

        # check substrings of length 2
        start, i = 0, 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2
            i = i + 1

        # check substrings with length greater than 2
        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1
                if (table[i + 1][j - 1] and s[i] == s[j]):
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
                i = i + 1
            k = k + 1

        substring = s[start:start + max_length]
        return substring