class Solution:
    def firstUniqChar(self, s: str) -> int:
        counth1 = {}
        count = 0
        for i in range(len(s)):
            counth1[s[i]] = 1 + counth1.get(s[i],0)
        for c in counth1:
            if counth1[c] == 1:
                print(c)
                return s.index(c)
            else:
                count+=counth1[c]
        if count == len(s):
            return -1