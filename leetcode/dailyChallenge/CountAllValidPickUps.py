class Solution:
#   https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
    def countOrders(self, n: int) -> int:
        res, mod = 1, 10**9 + 7
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) / 2 % mod
        return int(res)
        
