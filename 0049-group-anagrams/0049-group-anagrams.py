class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = defaultdict(list)
        
        for s in strs:
            char_set = [0] * 26
            for c in s:
                char_set[ord(c) - ord('a')] += 1
            hsh[tuple(char_set)].append(s)
        return list(hsh.values())