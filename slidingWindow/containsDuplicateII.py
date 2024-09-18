class Solution:
    #https://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=sliding-window
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_ = {}
        for key,val in enumerate(nums):
            if val in dict_ and key - dict_[val] <=k:
                return True
            else:
                dict_[val] = key
        return False