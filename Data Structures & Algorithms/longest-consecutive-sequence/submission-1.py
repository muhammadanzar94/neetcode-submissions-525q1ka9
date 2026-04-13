class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        h_map = {}
        if(n < 2):
            return n

        for i in range(n):
            h_map[nums[i]] = True
        
        max_count = 0

        for key in h_map:
            k = key
            count = 1

            while(True):
                if k+1 in h_map:
                    count+=1
                    k+=1
                else:
                    if(count>max_count):
                        max_count = count
                    break
                    
        return max_count
