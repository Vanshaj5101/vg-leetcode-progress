class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # s1_len = len(s1)
        # s2_len = len(s2)
        # if s1_len > s2_len:
        #     return False

        # s1 = ''.join(sorted(s1))

        # for i in range(s2_len-s1_len+1):
        #     substring = s2[i:s1_len + i]
        #     substring = ''.join(sorted(substring))
        #     if s1 == substring:
        #         return True
        # return False


        # sliding window approach 2

        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(s1_len):
            s1_freq[ord(s1[i]) - ord('a')] += 1
        
        i = j = 0
        while j < s2_len:
            s2_freq[ord(s2[j]) - ord('a')] += 1
            if j-i+1>s1_len:
                s2_freq[ord(s2[i]) - ord('a')] -= 1
                i += 1
            if s1_freq == s2_freq:
                return True
            j += 1
        return False
