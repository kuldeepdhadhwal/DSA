class Solution:
    #https://leetcode.com/problems/n-th-tribonacci-number/
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a
