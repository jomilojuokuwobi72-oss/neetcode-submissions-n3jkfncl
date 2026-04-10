class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1) ]

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)
        
        for num, i in hashmap.items():
            freq[i].append(num)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res
        
        return -1
            