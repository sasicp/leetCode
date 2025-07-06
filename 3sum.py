from collections import defaultdict

class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        two_sum =defaultdict(set)
        three_sum = set()
        for ii,num in enumerate(nums):
            for jj, num2 in enumerate(nums[ii+1:], ii+1):
                two_sum[num + num2].add(tuple(sorted([ii, jj])))
        for ii,num in enumerate(nums):
            if -num in two_sum:
                for t in two_sum[-num]:
                    if ii not in t:
                        three_sum.add(tuple(sorted((num,)+(nums[t[0]], nums[t[1]]))))

        return list(list(x) for x in three_sum)


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[-1,0,1,2,-1,-4]))
    print(solution.threeSum(nums=[0, 1, 1]))

