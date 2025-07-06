from collections import defaultdict


class Solution:
    def two_sum(self, nums: list[int], target: int, num_dict: defaultdict[int]):
        solutions = set()
        if not num_dict:
            for num in nums:
                num_dict[num] += 1

        for num in num_dict.keys():
            diff = target - num
            if diff in num_dict:
                if diff ==num:
                    if num_dict[diff] > 1:
                        solutions.add((diff, diff))
                else:
                    solutions.add((min(num, diff), max(num, diff) ))
        return list(([min(x), max(x)] for x in solutions))



    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sum = set()
        two_sum_d = defaultdict(int)
        for ii,num in enumerate(nums):
            res = self.two_sum(nums, -num, two_sum_d)
            for res1 in res:
                if num in res1 and two_sum_d[num] <= res1.count(num):
                    continue
                three_sum.add(tuple(sorted([num] + res1)))
        return list(list(x) for x in three_sum)


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[-1,0,1,2,-1,-4]))
    print(solution.threeSum(nums=[0, 1, 1]))
    print(solution.threeSum(nums=[-1, 0, 1, 0]))

