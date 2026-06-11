class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}

        for i in nums:
            if check.get(i) == 1:
                return True
            check[i] = check.get(i, 0) + 1
        return False
        