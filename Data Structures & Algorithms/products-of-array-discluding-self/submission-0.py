class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        solution is using prefix and suffix 
        [1,2,3,4]
        [1,1,1,1]
        prefix [1,2,6,24]
        suffix [24,24,12,4]
        '''
        result = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
             
        