class Solution:
#   https://leetcode.com/problems/length-of-last-word/
    def lengthOfLastWord(self, s: str) -> int:
        output = []
        for i in s.split(' '):
            if len(i.strip()) > 0:
                output.append(i.strip())
        return len(output[::-1][0])
