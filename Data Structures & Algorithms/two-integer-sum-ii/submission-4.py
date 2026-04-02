class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        left pointer and right pointer 
        left pointer starts at 0 
        right pointer starts at left plus 1 
        iterate through the whole array 
        return if you get target 
        else just keep going until it is returned 
        '''

        for l in range(len(numbers)):
            for r in range(l+1,len(numbers)):
                sum = numbers[l] + numbers[r]
                if sum == target:
                    return [l+1,r+1]

            
            