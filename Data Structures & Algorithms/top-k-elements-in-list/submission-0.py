from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [0] * 2001

        # Count frequencies
        for num in nums:
            count[num + 1000] += 1

        result = []

        # Repeat k times
        for _ in range(k):
            max_freq = max(count)
            idx = count.index(max_freq)   # index of that frequency
            result.append(idx - 1000)     # convert back to original number
            count[idx] = 0                # reset so we don't pick it again

        return result
