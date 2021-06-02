"""Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/plus-one/
"""

digits = list(map(int, input().split()))
num = int(''.join(list(map(str, digits)))) + 1
result = [int(i) for i in str(num)]
print(result)