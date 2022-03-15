class Solution:
    #https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        substr = list(s)
        print(substr)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                
            if s[i] == ')':
                if len(stack) !=0:
                    stack.pop()
                else:
                    substr[i] = ""
        print(substr)
        print(stack)
        for i in stack:
            substr[i] = ""
        
        return "".join(substr)
