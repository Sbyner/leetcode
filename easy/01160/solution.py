class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for w in words:
            subc = chars
            for c in w:
                subc=subc.replace(c,,1)
            if len(chars)-len(subc) == len(w):
                count += len(w)
        return count
