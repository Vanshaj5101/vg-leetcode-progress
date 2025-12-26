class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hshmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in hshmap.keys():
                if not stk or hshmap[c] != stk[-1]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return True if not stk else False
        