class Solution:
#   ` https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            print(i,num)
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
