'''
https://www.interviewbit.com/problems/distribute-candy/
Greedy Algorithms

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        candies = [1]*n

        for i in range(1, n):
            if A[i] > A[i-1]:
                candies[i] = candies[i-1]+1
        
        for j in range(n-2,-1,-1):
            if A[j]>A[j+1] and candies[j]<=candies[j+1]:
                candies[j] = candies[j+1] + 1

        return sum(candies)

