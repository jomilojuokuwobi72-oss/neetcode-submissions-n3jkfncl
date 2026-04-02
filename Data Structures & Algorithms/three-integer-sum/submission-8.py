class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort array 
        iterate through array of numbers
        have a left pointer starting at i + 1 
        have a right pointer at the end 
        while left < right pointer 
        calculate the sum 
        when the sum is equal to zero
        add that to the array 
        check for duplicates by making sure l,r,i do not use
        the same number sequence 
        '''
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1 #starts after i 
            r = len(nums)-1 # starts at the end of nums
            #Calculate total
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l +=1 
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif total > 0:
                    r = r - 1
                else:
                    l = l + 1 
            
        return result

