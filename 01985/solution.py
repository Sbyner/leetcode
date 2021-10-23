class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ints = list(map(int, nums))
        ints.sort()
        return str(([x for x in reversed(ints)][k-1]))
