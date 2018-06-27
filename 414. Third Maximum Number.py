class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hi = mid = low = float('-inf') 
        check_num = {}
        
        for i in range(len(nums)):
            
            x = nums[i]
            if x in check_num:
                continue
            else:
                check_num[x] = 1
            if x > hi:
                low = mid
                mid = hi
                hi = x
            elif x > mid:
                low = mid
                mid = x
            elif x > low:
                low = x
        if len(check_num) < 3:
            return hi
        else:
            return low
            
        
        
        