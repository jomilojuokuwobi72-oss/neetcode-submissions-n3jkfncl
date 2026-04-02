class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        [1,2,3,4]
        [5,6,7,8]
        [9,10,11,12]
        '''


        l = 0 
        r = len(matrix) -1 
        while l <= r:
            m = (l + r) // 2 
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                #perform binary search here 
                left = 0 
                right = len(matrix[m])-1
                while left <= right:
                    middle = (left + right) // 2 
                    if target == matrix[m][middle]:
                        return True
                    elif target < matrix[m][middle]:
                        right = middle - 1 
                    else:
                        left = middle + 1
                return False
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        return False