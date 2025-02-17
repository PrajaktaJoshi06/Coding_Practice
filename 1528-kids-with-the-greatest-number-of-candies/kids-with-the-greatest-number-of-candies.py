class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        res = []
        for i in candies:
            if extraCandies + i >= maxcandies:
                res.append(True)
            else:
                res.append(False)
        return res
        
