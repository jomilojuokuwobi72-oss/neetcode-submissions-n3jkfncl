class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        store the count in a hashmap of each number 
        Example 
        {1:1, 2:3, 3:3} {number: occurence}
        Make an array the size of dictionary or maybe nums and store the
        number where it occured essentially
        [[],[1],[],[2,3]]
        '''
        hashmap = {}
        arr = [[] for num in range(len(nums)+1)] # the max anything will ever occur is the length of the array 
        result = []
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
        
        for num, occurence in hashmap.items():
            arr[occurence].append(num)
        
        for i in range(len(arr)-1,-1,-1):
            for num in arr[i]:
                result.append(num)
            if len(result) == k:
                return result
        

        

