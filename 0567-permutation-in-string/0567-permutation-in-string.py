class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        s1 = ''.join(sorted(s1))

        for i in range(s2_len-s1_len+1):
            substring = s2[i:s1_len + i]
            substring = ''.join(sorted(substring))
            if s1 == substring:
                return True
        return False
