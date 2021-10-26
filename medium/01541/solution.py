class Solution:
    def minInsertions(self, s: str) -> int:
        q = deque()
        prev = False
        res = 0
        for p in s:
            if p == '(':
                if prev:
                    res += 1
                    prev = False
                    if q:
                        q.pop()
                    else:
                        res += 1
                q.append(p)
            elif p == ')':
                if not prev:
                    prev = True
                else:
                    prev = False
                    if q:
                        q.pop()
                    else:
                        res += 1
        if prev:
            res += 1
            if q:
                q.pop()
            else:
                res += 1
        res += len(q) * 2
        return res
                
