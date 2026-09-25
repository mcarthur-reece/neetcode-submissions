class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d.get(complement),i]
            d.setdefault(nums[i],i)
        return []