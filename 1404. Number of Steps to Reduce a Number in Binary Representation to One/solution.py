class Solution:
    def numSteps(self, s: str) -> int:
        dec = int(s,2)
        count = 0
        # print(dec)
        while dec != 1:
            if dec%2 == 0:
                dec//=2
                count+=1
            else:
                dec+=1
                count+=1
        return count