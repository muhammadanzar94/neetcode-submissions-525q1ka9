class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        h_map = {}

        for i in range(length):
            diff = target - nums[i]
            if diff in h_map:
                return [h_map[diff], i]
            h_map[nums[i]] = i
        
