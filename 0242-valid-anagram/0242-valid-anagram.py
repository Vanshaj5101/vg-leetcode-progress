class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = defaultdict()
        t_char = defaultdict()

        for i in range(len(s)):
            s_char[s[i]] = s_char.get(s[i], 0) + 1
            t_char[t[i]] = t_char.get(t[i], 0) + 1
        
        for k in s_char.keys():
            if s_char[k] != t_char.get(k, 0):
                return False
        return True