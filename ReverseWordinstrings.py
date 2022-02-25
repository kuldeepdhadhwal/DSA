class Solution:
#   `https://leetcode.com/problems/reverse-words-in-a-string-iii/
    def reverseWords(self, s: str) -> str:
        out = []
        l_str = s.split(" ")
        l = len(l_str)-1
        s=""
        for key,i in enumerate(l_str):
            s +=i[::-1]
            if key < l:
                s +=' '
            
        return s
