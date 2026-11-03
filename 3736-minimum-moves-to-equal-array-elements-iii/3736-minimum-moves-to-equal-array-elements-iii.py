class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        moves = 0

        for num in nums:
            moves += max_num - num

        return moves    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna