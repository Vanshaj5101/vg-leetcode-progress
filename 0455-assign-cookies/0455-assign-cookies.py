class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie = 0
        child = 0
        count = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                count += 1
                child += 1
            cookie += 1
        return count
        