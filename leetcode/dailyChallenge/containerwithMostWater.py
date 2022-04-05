class Solution:
#     https://leetcode.com/problems/container-with-most-water/

'''
Steps for Algorithm
1. First take i,j as a pointer representing the initial and end,
2. Then using a while loop runs till i < j
3. take max of water having water, min of i, j height by multiplying it with j-i
4. check the height and update the i if height[i] < height[j] else j-=1

'''
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        water = 0
        while i < j:
            water = max(water,(j-i)*min(height[i],height[j]))
            if height[i] < height[j]:
                i+=1
            else:
                j -=1
        return water
