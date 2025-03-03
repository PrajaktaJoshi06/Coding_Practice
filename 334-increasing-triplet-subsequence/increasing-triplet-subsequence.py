class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pt1 = float('inf')
        pt2 = float('inf')
        for n in nums:
            if n <= pt1:
                pt1 = n
            elif n<= pt2:
                pt2 = n
            else: 
                return True
        return False

        