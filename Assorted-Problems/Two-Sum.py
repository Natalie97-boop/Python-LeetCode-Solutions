class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        indexes = {}
        
        for i in range(len(nums)):
            if target - nums[i] in indexes:
                return [indexes[target - nums[i]],i]
            else:
                indexes[nums[i]]=i 