from itertools import islice    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(dict(Counter(nums)).items())
        count.sort(key=lambda x: x[1])
        return islice([x[0] for x in reversed(count)], None, k)
