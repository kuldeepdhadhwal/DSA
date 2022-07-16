# Problem link
#https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Solution Explanation
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")
        def maxpath(node):
            nonlocal max_path
            if node is None:
                return 0
            left_max = max(maxpath(node.left),0)
            right_max = max(maxpath(node.right),0)
            current_max = node.val + left_max + right_max
            max_path = max(current_max,max_path)
            
            return node.val + max(left_max,right_max)
    
        maxpath(root)
        return max_path
            
