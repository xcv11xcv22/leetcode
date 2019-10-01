class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        _len = len(s)
        if _len == 1:
            return s
        if _len == 0:
            return ''
        find = 0
        for i in range(_len-1):
            if (s[0] == s[i+1]):
               find = i+2
            else:
               
                break
        ansStr= s[0]
        if find:
            ansStr = s[0:find]
       
        ct = 1
        _type = 0
        for i in range(1,_len):
            ct = 1
            while 1:
                if i-ct >=0 and i+ct < _len and s[i-ct] == s[i+ct]  :
                    ct+=1
                   # print(1)
                else:
                  #  print(ct)      
                    if ct == 1:
                        break
                    pos = ct -1
                    #print(666)  
                    if len(ansStr) <  (i+pos+1)-(i-pos):
                        ansStr =s[i-pos:i+pos+1]
                    break
    #                    if ansStr == 'baba':
    #                        print((i,pos))
                    
            ct = 1
            while 1:

                if i-ct+1 >=0 and i+ct < _len and s[i-ct+1] ==  s[i+ct] :
                    ct +=1
                  #  print(3) 
                else:
                   # print(4) 
                    if ct == 1:
                        break

                    pos = ct -1

                    if len(ansStr) <  (i+pos+1)-(i-pos+1):
                        ansStr=s[i-pos+1:i+pos+1]
    #                    if ansStr == 'baba':
    #                        print((i,ct,'b'))
                    break
                    
        return ansStr