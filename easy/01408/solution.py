class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words.sort(key=lambda w: len(w))
        print(words)
        for i,word in enumerate(words):
            if any(word in w for w in words[i+1:]):
                res.append(word)
        return res
