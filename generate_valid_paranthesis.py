# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrack solution
        # created a two empty list
        # if openN < n then openN+1, closedN, if closedN < openN then openN, closedN + 1, if openN == closedN == n return
        openN = 0
        closedN = 0
        stack = []
        res = []
        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(openN,closedN)
        return res
