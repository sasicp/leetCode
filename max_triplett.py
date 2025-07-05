class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i_pos = 0
        j_pos = 1
        k_pos = 2
        def comp_cost():
            return (nums[i_pos] - nums[j_pos])*nums[k_pos]
        if len(nums)<3:
            return 0
        max_cost = comp_cost()


