class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_one, pointer_two = 0, len(numbers) - 1

        for _ in range(len(numbers)):
            total = numbers[pointer_two] + numbers[pointer_one]
            if total == target:
                return [pointer_one + 1, pointer_two + 1]
            elif total < target:
                pointer_one += 1
            else:  
                pointer_two -=1