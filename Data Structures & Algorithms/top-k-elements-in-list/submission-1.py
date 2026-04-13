class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        length = len(nums)
        h_map = {}

        for i in range(length):
            if nums[i] not in h_map:
                h_map[nums[i]] = 1
            else:
                h_map[nums[i]] += 1

        
        sorted_h_map = (sorted(h_map.items(), key=lambda x:x[1], reverse = True))
        arr = sorted_h_map[:k]
        return[x[0] for x in arr]