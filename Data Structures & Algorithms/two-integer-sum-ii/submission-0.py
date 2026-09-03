class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_one, pointer_two = 0, len(numbers) - 1

        while pointer_one < pointer_two:
            if numbers[pointer_two] + numbers[pointer_one] == target:
                return [pointer_one + 1, pointer_two + 1]
            elif numbers[pointer_two] + numbers[pointer_one] < target:
                pointer_one += 1
            else:  
                pointer_two -=1