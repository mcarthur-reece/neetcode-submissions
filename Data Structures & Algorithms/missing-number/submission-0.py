class Solution:
   
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            print(xorr)
            xorr ^= i ^ nums[i]
        return xorr