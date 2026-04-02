class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashmap = {}
       '''
        hashmap = {
                3: 0
                4: 1
                number and index 
            }
       '''
       for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[num] = i

        