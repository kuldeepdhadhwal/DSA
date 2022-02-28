class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # https://leetcode.com/problems/power-of-two/
        # return n and not (n & n - 1)
        if n == 0:
            return False
        return ((n==1) or (n%2==0 and self.isPowerOfTwo(n/2)))
