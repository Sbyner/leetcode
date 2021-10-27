class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(c , n):
            return chr((ord(c) - 97 + n) % 26 + 97)
        sm = 0
        res=
        for c,sh in zip(reversed(s),reversed(shifts)):
            sm += sh
            res = shift(c,sm) + res
        return res
