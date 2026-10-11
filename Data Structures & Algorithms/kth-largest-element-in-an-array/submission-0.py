class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using sorting
        return sorted(nums)[-k]