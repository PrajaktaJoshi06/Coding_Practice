class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        pivots = []
        ans = []
        i = 0
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            elif i == pivot:
                pivots.append(i)

        ans.extend(left)
        ans.extend(pivots)
        ans.extend(right)
        return ans
        