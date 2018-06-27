# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.val_All= 0
        
        self.ans = 0
        self.unique = set()
    def findNode(self,node,sum,max):
        if node is None:
            return
        
        
        if node.val - sum == 0 :
            self.ans +=1
        if node.val == max and node not in self.unique:
            self.ans +=1
        if node.left is not None:
            self.findNode(node.left,sum-node.val,max)
        if node.right is not None:
            self.findNode(node.right,sum-node.val,max)
     
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        if root is None:
            return 0
        nodes = [None,root]
        idx = 1
        while idx < len(nodes):
            if nodes[idx] is not None and (nodes[idx].left is not None or nodes[idx].right is not None):
                nodes.append(nodes[idx].left)
                nodes.append(nodes[idx].right)
            
            idx+=1
        _len = len(nodes)-1
        if _len == 1 and nodes[1].val == sum:
            return 1
        elif _len == 1:
            return 0
        self.findNode(nodes[1],sum,sum)
        self.findNode(nodes[1].left,sum,sum)
        self.findNode(nodes[1].right,sum,sum) 
        return self.ans
       
        return (_len)
        for i in range(_len,0,-1):            
            if nodes[i] is None:
                continue
         
            self.val_All = 0
            self.findNode(nodes[i],sum)  
      
        return self.ans