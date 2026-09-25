class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = [0] * len(nums)
        for i in range(len(nums)):
            x = 1
            for j in range(0,len(nums)):
                if i != j:
                    x *= nums[j]
            n[i] = x
            print(n[i])
        return n