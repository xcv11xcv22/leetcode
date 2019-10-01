# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        global head
        head = root
        global ans
        global find
        find = False
        ans =0
        def findChild(node,sum,level):
            global find
            global ans
            global head
            ans += node.val
            if ans == sum and  node.left is None and  node.right is  None:
                
                
                find = True
                return
            
           
            
            if node.left is not None:       
                findChild(node.left,sum,level+1)
              
            if node.right is not None:
              
                findChild(node.right,sum,level+1)
            
            ans-= node.val
        findChild(head,sum,1)
        # if ans == 1 and root.left is not None and root.left.val == 2:
        #     return (find,ans)
        # else:
        return find
        
        
        
        