class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        useChar = {}
        maxlength = 1
        start = 0
        _str = ''
        for i in range(len(s)):
            if s[i] in useChar :
                if   s[start:i+1].count(s[i]) > 1:
                    maxlength = max(i -start,maxlength)
                else:
                    maxlength = max(i -start+1,maxlength)

                if useChar[s[i]] + 1  > start :
                  start = useChar[s[i]] +1
                      
                useChar[s[i]] = i  
           
            else:

               useChar[s[i]] = i
    
               maxlength = max(i -start+1,maxlength)
               if   s[start:i+1].count(s[i]) > 1:
                  maxlength = max(i -start,maxlength)
               else:
                  maxlength = max(i -start+1,maxlength) 
           
        return maxlength