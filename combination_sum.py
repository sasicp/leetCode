from typing import List
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb_sum(cands, target_sub, comb_so_far):
            out = set()
            if target_sub < 0:
                return tuple()
            if target_sub == 0:
                return tuple(sorted(comb_so_far))
            for num in cands:
                comb_so_far.append(num)
                sols = comb_sum(cands, target_sub - num, comb_so_far)
                if sols:
                    if isinstance(sols, set):
                        out = out | sols
                    elif isinstance(sols, tuple):
                        out.add(sols)
                comb_so_far.pop()
            return out
        out_set =  comb_sum(candidates, target,[])
        return [list(x) for x in out_set]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    print(s.combinationSum([2,3,5], 8))
    print(s.combinationSum([2], 1))