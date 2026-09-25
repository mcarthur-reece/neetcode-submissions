class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) < 1:
            return 0
        
        nums.sort()
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        currMax = 1
        totalMax = 1
        print(nums)
        for i in range(1, len(nums)):
            print(nums[i])
            print(str(currMax) + " this is currMax before for loop")
            if abs(nums[i] - nums[i-1]) == 1:
                currMax += 1
            else:
                totalMax = max(currMax, totalMax)
                currMax = 1
            print(str(currMax) + " this is currMax after for loop")
            totalMax = max(currMax, totalMax)
            
        return max(totalMax, currMax)