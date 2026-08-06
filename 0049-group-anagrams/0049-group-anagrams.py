class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hshmap = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            hshmap[tuple(arr)].append(s)
        
        return [lst for key, lst in hshmap.items()]