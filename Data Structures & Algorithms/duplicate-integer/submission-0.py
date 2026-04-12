class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        length = len(nums)
        harr = {}

        for i in range(length):

            if nums[i] in harr:
                return True
            else:
                harr[nums[i]] = True 
        print(harr)
        return False