'''
Generate Parentheses
medium

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:
Input: n = 1

Output: ["()"]
Example 2:
Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]

You may return the answer in any order.
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return result