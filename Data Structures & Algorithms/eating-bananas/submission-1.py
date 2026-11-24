class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right 
        while left <= right: 
            k = left + (right - left) // 2
            total = 0
            for p in piles:
                total += p // k + (1 if p % k > 0 else 0) #this counts the amount of time to finish everything
            if total <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res