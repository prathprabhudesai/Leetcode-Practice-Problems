/*
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 Example 1:

 Input: x = 121
 Output: true
 Example 2:

 Input: x = -121
 Output: false
 Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
 Example 3:

 Input: x = 10
 Output: false
 Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 Example 4:

 Input: x = -101
 Output: false


  Constraints:

  -231 <= x <= 231 - 1
*/

#include <math.h>
#include <limits.h>

bool isPalindrome(int x)
{
    if ((x > INT_MAX) || (x < 0)) {
        return false;
    }
    unsigned int i, j;
    int count = 0, digit;
    int digit_track[15];
    while(x != 0)
    {
        digit = x%10;
        digit_track[count] = digit;
        x = (x-digit)/10;
        count++;
    }

    i = 0;
    j = count - 1;
    while ((i != j) && (i < count) && (j >= 0))
    {
        if (digit_track[i] != digit_track[j])
        {
            return false;
        }
        i++;
        j--;
    }
    return true;
}
