class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict(Counter(s))
        res = [s.find(x) for x in count if count[x] == 1]
        return min(res) if len(res)>0 else -1
