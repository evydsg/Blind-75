class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDictionary = {}

        for num in nums:
            if num in numsDictionary:
                return True
            else:
                numsDictionary[num] = 1

        return False