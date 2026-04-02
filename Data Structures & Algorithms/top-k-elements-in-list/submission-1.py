class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = {}
        arr = [[] for num in range(len(nums)+1)]
        result = []
        # add values in hashmap in the form of number: occurence 
        for num in nums:
            occurence[num] = 1 + occurence.get(num,0) 
        
        # store these into the array where they belong
        # for example a number that occured twice will be stored at index two in the list 
        for num, count in occurence.items():
            arr[count].append(num)


        # add k most frequent elements now that it is in the required format
        # [[1][2,3]]
        for bucket in reversed(arr):
            for num in reversed(bucket):
                result.append(num)
                if len(result) == k:
                    return result
            
        
