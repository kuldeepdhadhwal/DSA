class Solution:
    # https://leetcode.com/problems/maximum-subarray/
    # get current max_sum as first num, current sum as 0
    # iterate over nums, add sum, find out max between max_sum, current_sum if current_sum < 0 then current_sum = 0 
    # return max_sum
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum = current_sum + num

            max_sum = max(max_sum , current_sum)

            if current_sum < 0:

                current_sum = 0

        return max_sum
