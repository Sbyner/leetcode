class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        d = 0
        prev = nums[0]
        for v in nums:
            if prev < v:
                if d == -1:
                    return False
                d = 1
            elif prev > v:
                if d == 1:
                    return False
                d = -1
            prev = v
        return True
