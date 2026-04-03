class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        for this, we will perform a binary search 
        left at beginning, right at end 
        middle is left + right divided by 2 
        if middle is greater than whatever is on the right side 
        we know that the minimum is on the right side 
        left is middle + 1 
        else if the middle is less than that but greater than what is on the left side 
        we know the minimum is on the left 
        we return the left index 
        '''
        left = 0 
        right = len(nums) - 1
        while left < right: 
            middle = (left + right) // 2 
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle 
        return nums[left]