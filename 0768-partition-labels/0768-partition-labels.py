class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hshmap = defaultdict(int)

        for i in range(len(s)):
            hshmap[s[i]] = i
        
        output = []
        size = 0
        end = 0

        for i in range(len(s)):
            size += 1
            end = max(hshmap[s[i]], end)
            if i == end:
                output.append(size)
                size = 0
                end = 0
        return output