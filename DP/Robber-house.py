class Solution:
#     https://leetcode.com/problems/house-robber/submissions/
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for num in nums:
            temp = prev # This represents the nums[i-2]th value
            prev = curr # This represents the nums[i-1]th value
            curr = max(num + temp, prev) # Here we just plug into the formula
        return curr
            
