class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        I think I would do a binary search twice 
        one with each array 
        and then one with each of the n elements within the array
        one thing tho:
            let's say I look in one array and the number I am looking for is 
            not in that range of its first and last element 
            then I move on
        '''
        l = 0
        r = len(matrix) - 1 
        while l <= r:
            m = (l + r) // 2 
            left = 0
            right = len(matrix[m]) -1
            if target >= matrix[m][left] and target <= matrix[m][right]:
                # perform binary search here
                while left <= right:
                    middle = (left + right) // 2 
                    if matrix[m][middle] == target:
                        return True
                    elif matrix[m][middle] > target:
                            right = middle - 1
                    else:
                        left = middle + 1
                return False
            elif target > matrix[m][right]:
                l = m + 1
            else:
                r = m - 1
        return False