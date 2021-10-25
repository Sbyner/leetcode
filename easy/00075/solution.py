class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i0 = -1
        i2 = len(nums)
        for v in nums:
            if v == 0:
                i0 += 1
            if v == 2:
                i2 -= 1
        for i in range(len(nums)):
            if i <= i0:
                nums[i] = 0
            elif i < i2:
                nums[i] = 1
            else:
                nums[i] = 2
