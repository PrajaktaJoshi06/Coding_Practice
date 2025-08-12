class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [dict[diff], i]
            dict[n] = i
        return []
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []








