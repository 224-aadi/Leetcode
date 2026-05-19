class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_list = []

        for idx, num in enumerate(nums):
            to_find = target - num
            if to_find in nums:
                find_idx = nums.index(to_find)
                if find_idx != idx:
                    idx_list.append(idx)
                    idx_list.append(find_idx)
                    idx_list.sort()
                    return idx_list

        