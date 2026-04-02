class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        check if it is a starting sequence meaning 
        if its number - 1 is not in the set then it is a starting sequence

        check if it's number plus 1 is in the set and keep going until it is not 

        Store this in a count 

        return the max count 
        '''
        numbers = set(nums)
        maxNum = 0
        current = 0

        for num in nums:
            if (num-1) not in numbers:
                cal = num + 1
                current = 1
                while cal in numbers:
                    cal+= 1
                    current += 1
            maxNum = max(maxNum,current)
        return maxNum


