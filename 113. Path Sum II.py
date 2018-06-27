# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        idx = 0
        if root is None:
            return []
        ans = []
        
        nodes = [(root,root.val,[root.val])]
        a = 0
        while idx < len(nodes):
            end = 0
            _tmpList = nodes[idx][2][:]
            if nodes[idx][0].left is not None:
                _tmpList.append(nodes[idx][0].left.val)
               
                nodes.append((nodes[idx][0].left,nodes[idx][1]+nodes[idx][0].left.val,_tmpList))
                end += 1
            _tmpList = nodes[idx][2][:]
            if nodes[idx][0].right is not None:
                _tmpList.append(nodes[idx][0].right.val)
                nodes.append((nodes[idx][0].right,nodes[idx][1]+nodes[idx][0].right.val,_tmpList))
                end += 1
            if nodes[idx][1] == sum  and end == 0:
           
                ans.append(nodes[idx][2])
                
                
            idx+=1
        return ans#[len(nodes)-1]  
        return 1
       