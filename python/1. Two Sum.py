class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic_ans = {}
        
        for i in range(len(nums)):
            if target - nums[i] in dic_ans:
                return [dic_ans[target - nums[i]],i]
            
            else:
                dic_ans[nums[i]] = i
                
                