class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        use binary search to do so
        left = 0 
        right = length of array  
        while left < right: 
            middle is left + right // 2
            if middle == target:
                return middle 
            elif middle < target:
                right = middle - 1
            else:
                left = middle + 1 
                [1,2,3,4,5,6]
                l = 0
                r = 6
                m = 4
                l = 0
                r = 3
        '''
        l = 0 
        r = len(nums) - 1
        while l <= r:
            # [1,2,3,4,5,6]
            middle = (l + r) // 2
            print(middle) 
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
        return -1