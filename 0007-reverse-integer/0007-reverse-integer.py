class Solution:
    def reverse(self, x: int) -> int:
        min = -2**31
        max = 2**31-1
        n = 0
        multi = 1
        if x < 0:
            multi = -1
            x *= -1
        while True:
            if n < min/10 or n > max/10:
                return 0
            n = (10 * n) + (x%10)
            x = x // 10
            if x == 0:
                break
        return multi * n