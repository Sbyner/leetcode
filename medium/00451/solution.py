class Solution:
    def frequencySort(self, s: str) -> str:
        res=
        count = list(dict(Counter(s)).items())
        count.sort(key=lambda x: x[1])
        for c in reversed(count):
            for r in range(c[1]):
                res += c[0]
        return res
