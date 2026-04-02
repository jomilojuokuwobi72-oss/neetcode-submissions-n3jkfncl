class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [1,2,3,4,5,6,7,8,9,10] target = 7
        [2,3,4] target = 6
        '''
        left = 0
        right = len(numbers) - 1

        while left < right:
            addition = numbers[right] + numbers[left]
            if addition == target:
                return [left+1,right+1]
            elif addition > target:
                right-= 1
            elif addition < target:
                left+=1
