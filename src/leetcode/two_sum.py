class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx, i in enumerate(nums[:-1]):
            for idx_j, j in enumerate(nums[idx + 1 :]):
                if i + j == target:
                    return [idx, idx + 1 + idx_j]
        return []
