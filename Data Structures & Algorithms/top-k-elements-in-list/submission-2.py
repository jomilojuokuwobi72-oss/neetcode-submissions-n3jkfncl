class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        store in a hashmap with the number and its occurence 
        create a list the size of the array itself and 
        store each number with how much it occured 
        {
            1: 1
            2: 2
            3: 3
            4: 3
        }
        [[][1][2][3,4][][]]
        k = 2
        returns [3,4]
        '''

        result = [[] for _ in range(len(nums)+1)]
        print(len(result))
        occurence = {}
        answer = []

        for n in nums:
            occurence[n] = 1 + occurence.get(n,0)
        
        for num, count in occurence.items():
            result[count].append(num)
        
        for bucket in reversed(result):
            for num in bucket:
                answer.append(num)
                if len(answer) == k:
                    return answer
        
        return answer


       