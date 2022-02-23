class Solution:
    
    https://leetcode.com/problems/reverse-string/submissions/
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for key,i in enumerate(s[::-1]):
            s[key]=i
        print(s)
