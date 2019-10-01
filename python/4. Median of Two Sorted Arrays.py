class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       
        if nums1 is None:
            nums1 = []
        if nums2 is None:
            nums2 = []    
        twoLen = len(nums1) + len(nums2) 
   
        nums1.extend(nums2)
        if twoLen % 2 == 0:
            return sum(nums1)/len(nums1)
        else:
            nums1.sort()
            return nums1[len(nums1)//2]