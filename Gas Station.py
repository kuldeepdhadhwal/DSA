'''
https://www.interviewbit.com/problems/gas-station
Greedy Algorithm
Google, Deshaw, amazon, bloomberg
'''

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, petrol, dist):
        n = len(petrol)
        start,petrolsum,distsum = 0,0,0
        for i in range(n):
            petrolsum+=(petrol[i]-dist[i])
            distsum+=(petrol[i]-dist[i])
            if distsum<0:
                start=i+1
                distsum = 0
        if petrolsum>=0:return((start)%n)
        else:return(-1)
