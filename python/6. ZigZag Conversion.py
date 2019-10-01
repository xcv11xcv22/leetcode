class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        _ct = 0
        _len_s = len(s)
        _arrZig = []
        _go = True
        _idx = -1
        for i in range(numRows):
            _arrZig.append([])
        while _ct < _len_s:
           
            if _go:
                _idx+=1
            else:
                _idx-=1
            _arrZig[_idx].append(s[_ct])
         
            if _go and _idx +1 >= numRows or not _go and _idx <= 0:
                _go = not _go
            _ct +=1
        _ans = ''
        for l in _arrZig:
            _ans += ''.join(l)
       
        return _ans
                
            
            
            