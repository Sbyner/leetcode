# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mn = 1
        mx = n
        res = None
        while res != 0:
            res = guess((mx+mn)//2)
            if res == -1:
                mx = (mx+mn)//2
            elif res == 1:
                mn = (mx+mn)//2 + 1
        return (mx+mn)//2
