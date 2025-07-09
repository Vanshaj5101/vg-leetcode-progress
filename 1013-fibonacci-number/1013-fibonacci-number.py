class Solution:
    def fib(self, n: int) -> int:
        hshmap = {0:0, 1:1}
        def fibo(x):
            if x not in hshmap:
                hshmap[x] = fibo(x-1) + fibo(x-2)
            return hshmap[x]

        return fibo(n)
        