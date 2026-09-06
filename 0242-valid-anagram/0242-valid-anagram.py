class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_len = len(s)
        t_len = len(t)
        s_hshmap = defaultdict(int)
        t_hshmap = defaultdict(int)

        for i in range(len(s)):
            s_hshmap[s[i]] += 1
            t_hshmap[t[i]] += 1

        for c in s:
            if c not in t_hshmap or s_hshmap[c] != t_hshmap[c]:
                return False
        
        return True

        # TC : O(n)
        # SC : O(k) k <= 26