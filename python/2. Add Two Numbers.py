#Runtime: 136 ms
#速度算不快
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value = []
        ct = 0
        AnsNode = None
        for node in [l1,l2]:
            ct = 0
            while node != None:
                if len(value) == ct:
                    value.append(0)
                value[ct] += node.val
                ct+=1
                node = node.next
        
        test = []
        go = True
        ct = 0
        add = 0
        while 1:
            if len(value) == ct:
                value.append(0)
            x = value[ct] + add
          
          
            if ct != 0:
                
                v = x % 10
                add = int(x/10)
                test.append(v)
                TmdNode.next = ListNode(v)
                TmdNode = TmdNode.next
              
            else:
                v = x % 10
                add = int(x/10)
                test.append(v)
                AnsNode = ListNode(v)
                TmdNode = AnsNode
            if  x < 10 and ct >= len(value) -1:
                
               
                break
            ct +=1
            
            
        test = []
        while AnsNode != None:
            test.append(AnsNode.val)
            AnsNode = AnsNode.next
        return test
        
                
                
            