def area(pos1, pos2):
    return min(pos1[1], pos2[1]) * (pos2[0] - pos1[0])


class Solution:

    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        index1 = 0
        index2 = len(height) - 1

        while index2 - index1 > 0:
            curr_area = area((index1, height[index1]),
                                  (index2, height[index2]))
            if curr_area > max_area:
                max_area = curr_area
            if height[index1] > height[index2]:
                incr = -1
                cursor = index2 - 1
                while (height[cursor] <= height[index2]) and (cursor > index1):
                    cursor += incr
                index2 = cursor
                curr_area = area((index1, height[index1]),
                                      (index2, height[index2]))
                if curr_area > max_area:
                    max_area = curr_area
            else:
                incr = 1
                cursor = index1 + 1
                while (height[cursor] <= height[index1]) and (cursor < index2):
                    cursor += incr
                index1 = cursor
                curr_area = area((index1, height[index1]),
                                 (index2, height[index2]))
                if curr_area > max_area:
                    max_area = curr_area
        return max_area


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 2, 3, 4, 5]))
    print(sol.maxArea([1, 8, 6, 2,5,4,8,3,7]))
    print(sol.maxArea([1, 1]))