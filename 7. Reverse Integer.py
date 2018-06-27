class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _ans = 0
        negative = False
        if x < 0:
            x = abs(x)
            negative = True
        while x > 0 :
            _ans = _ans * 10 + x % 10
            x = int(x/10)
            
       
        
        if _ans > 2147483647:
            return 0
        if negative:
            _ans = 0 - _ans
        return _ans