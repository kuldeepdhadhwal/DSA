class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        zeroCounter = 0
        
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i +=1
            else:
                zeroCounter +=1
        while i < len(nums):
            nums[i] = 0
            i +=1
        
        print(nums)
                
