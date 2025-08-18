class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # pick all numbers except i and j
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                        # possible operations
                        for op in [nums[i] + nums[j], 
                                   nums[i] - nums[j], 
                                   nums[j] - nums[i], 
                                   nums[i] * nums[j]]:
                            if solve(next_nums + [op]):
                                return True
                        
                        # handle division carefully
                        if abs(nums[j]) > 1e-6:
                            if solve(next_nums + [nums[i] / nums[j]]):
                                return True
                        if abs(nums[i]) > 1e-6:
                            if solve(next_nums + [nums[j] / nums[i]]):
                                return True
            return False

        # convert input to float to avoid integer division issues
        return solve([float(c) for c in cards])