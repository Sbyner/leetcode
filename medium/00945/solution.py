class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] <= prev:
                print(nums[i], prev)
                res += prev - nums[i] + 1 
                nums[i] += prev - nums[i] + 1
            
            prev = nums[i]
        return res
