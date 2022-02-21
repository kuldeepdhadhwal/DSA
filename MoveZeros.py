class Solution:
    # https://leetcode.com/problems/move-zeroes/
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count +=1
        add = [0]*count
        for i in range(len(nums)):
            if nums[i] !=0:
                out.append(nums[i])
        
        print(out+add)
