class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = [0] * (len(nums))


        
        x = 1
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if i != j:
                    x *= nums[j]
                j -= 1
            n[i] = x
            x = 1



        return n 