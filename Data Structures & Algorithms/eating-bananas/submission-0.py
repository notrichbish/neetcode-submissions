class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right 
        while left <= right: 
            mid = left + (right - left) // 2
            total = 0
            for p in piles:
                total += p // mid + (1 if p % mid > 0 else 0) #this counts the amount of time to finish everything
            if total <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res