# Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()

# Solution 2


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            print(sortedString)
            if sortedString in myDict:
                myDict[sortedString].append(strs[i])
            else:
                myDict[sortedString] = [strs[i]]
        return myDict.values()
