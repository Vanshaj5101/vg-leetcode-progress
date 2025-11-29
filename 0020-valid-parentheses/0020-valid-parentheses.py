class Solution:
    def isValid(self, s: str) -> bool:
        hshmap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack or stack[-1] != hshmap[c]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False