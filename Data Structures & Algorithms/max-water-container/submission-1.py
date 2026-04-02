class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
         area = length * breadth 
         length = distance between i and i + n
         breadth = whichever height between left and right pointer is lower 
         maxArea = max(maxArea, area)
        '''
        '''
        o(n) squared - need to solve this in o(n)
        maxA = 0 # max area 

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                area = (j - i) * min(heights[i],heights[j])
                print(area)
                maxA = max(maxA,area)
        
        return maxA
        '''

        l = 0 
        r = len(heights) - 1 
        maxArea = 0
        while l < r:
            #length * height
            area =  (r-l) * min(heights[l],heights[r])
            maxArea = max(maxArea,area)
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        
        return maxArea


    

