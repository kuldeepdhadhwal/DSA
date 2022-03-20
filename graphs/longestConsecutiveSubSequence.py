class Solution:
#     https://leetcode.com/problems/longest-consecutive-sequence/
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums, ans = set(nums), 0
        for num in nums:
            print(num)
            print(num-1)
            if num - 1 in set_nums: continue
                
            nxt = num
            while nxt + 1 in set_nums:
                nxt += 1
            ans = max(ans, nxt-num+1)
                
        return ans
