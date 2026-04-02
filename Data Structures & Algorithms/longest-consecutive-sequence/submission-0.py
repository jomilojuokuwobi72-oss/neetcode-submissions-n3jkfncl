class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0 
        maxLength = 0
        for num in nums:
            # check if it is a start index
            if (num-1) not in numSet:
                length = 0
                while (num+length) in numSet:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength