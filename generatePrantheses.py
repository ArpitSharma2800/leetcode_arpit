# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Back Tracking

from typing import List
import sys
sys.setrecursionlimit(5000000)


def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []

    def backtraking(open, closed):
        if open == closed == n:
            res.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            backtraking(open + 1, closed)
            stack.pop()
        if closed < open:
            stack.append(")")
            backtraking(open, closed + 1)
            stack.pop()  # after backtracking function return

    backtraking(0, 0)
    return res


print(generateParenthesis(3))
