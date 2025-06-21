class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_speed = 1
        high_speed = max(piles)
        speed = high_speed

        while low_speed <= high_speed:
            mid = (high_speed + low_speed) // 2
            hr = self.check(mid, piles)
            if hr <= h:
                speed = mid
                high_speed = mid - 1
            else:
                low_speed = mid + 1
        return speed


    def check(self, mid_speed, piles) -> int:
        hrs = 0
        for p in piles:
            hrs += (math.ceil(p/mid_speed))
        return hrs


    