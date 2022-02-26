class Solution:
    #https://leetcode.com/problems/fibonacci-number/submissions/
    def fib(self, n: int) -> int:
        mem = [0,1]
        if n > 1:
            for i in range(n):
                mem.append(mem[i]+mem[i+1])
        return mem[n]
