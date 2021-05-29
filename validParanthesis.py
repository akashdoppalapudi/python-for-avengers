"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

--> Open brackets must be closed by the same type of brackets.
--> Open brackets must be closed in the correct order.

link : https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        match = {'[':']', '{':'}', '(':')'}
        parlist = []
        for i in s:
            if i in "[{(":
                parlist.insert(0, i)
                s = s.replace(i,'',1)
            try:
                if match[parlist[0]]==i:
                    parlist.pop(0)
                    s = s.replace(i,'', 1)
            except IndexError:
                return False

        if len(parlist)==0 and s=="":
            return True
        else:
            return False