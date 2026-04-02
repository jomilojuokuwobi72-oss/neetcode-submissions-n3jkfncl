class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        return sets of 3 in which their sum is zero
        no duplicates 
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        '''
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                '''
                need to make sure there are not duplicates 
                '''
                sol = nums[i] + nums[l] + nums[r]
                if sol == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l = l + 1 
                    r = r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r+1]:
                        r = r - 1
                elif sol > 0:
                    r = r - 1 
                else:
                    l = l + 1
        return result

            