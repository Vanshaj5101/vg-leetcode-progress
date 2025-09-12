class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sdict = defaultdict(int)
        tdict = defaultdict(int)

        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1
            tdict[t[i]] = tdict.get(t[i], 0) + 1
        
        for k,v in sdict.items():
            if sdict[k] != tdict.get(k, 0):
                return False
        
        return True