class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        s = s.split()[0]
        if not s[0].isdigit() and s[0] != '-' and s[0] != '+':
            return 0
        print(s)
        res = 0
        neg = False
        for i,c in enumerate(s):
            if c == '-' and i == 0:
                neg = True
                continue
            elif c == '+' and i == 0:
                continue
            if i != 0 and not c.isdigit():
                break
            if c.isdigit():
                res *= 10
                res += int(c)
        if neg:
            res *= -1
        if res <= -2**31:
            res = -2**31
        elif res >= 2**31 -1:
            res = 2**31 -1
        return res
