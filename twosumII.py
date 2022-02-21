class Solution:
    #https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        left = 0
        right = len(nums)-1
        leftvar = nums[left]
        rightvar = nums[right]
        
        while left <= right:
            sum_ = leftvar + rightvar
            if sum_ < target:
                left +=1
                leftvar = nums[left]
            elif sum_ > target:
                right -=1
                rightvar = nums[right]
            if sum_ == target:
                return [left+1,right+1]
