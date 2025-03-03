class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            else:
                pass
        for j in nums:
            if j == 0:
                nums.remove(j)
                nums.append(j)
            else:
                pass
        return nums
        