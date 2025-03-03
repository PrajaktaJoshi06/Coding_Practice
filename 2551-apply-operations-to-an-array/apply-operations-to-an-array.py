class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            else:
                pass
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
            else:
                pass
        return nums
        