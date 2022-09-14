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

#Second solution
def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for val in c:
            if c[val] == 1:
                return s.index(val)
        return -1
        
#Third solution
def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for v,k in enumerate(s):
            if c[k] == 1:
                return v
        return -1

#Fastest solution
def firstUniqChar(self, s: str) -> int:
    best = float('inf')
    for i in range(26):
        c = chr(i + ord('a')) #ord function returns ascii value and chr function returns it back to the character
        l = s.find(c) #returns index of character in paranthesis by swiping from left, if character is not there it returns -1
        r = s.rfind(c) #returns index of character in paranthesis by swiping from right, if character is not there it returns -1
        if l != -1 and l == r: 
            best = min(best, l)
    return best if best != float('inf') else -1
