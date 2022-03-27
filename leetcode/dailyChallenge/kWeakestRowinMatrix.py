class Solution:
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row, col = len(mat), len(mat[0])
        output = {}
        for i in range(row):
            count = 0
            for j in range(col):
                if mat[i][j] == 1:
                    count +=1
            output[i] = count
        marklist = sorted(output.items(), key=lambda x:x[1])
        sortdict = list(marklist)
        
        final_list = []
        for i in range(k):
            final_list.append(sortdict[i][0])
        
        return final_list
