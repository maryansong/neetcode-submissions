class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            count = i
            for x in nums[i+1:]:
                count += 1
                if nums[i] + x == target:
                    return [i, count]