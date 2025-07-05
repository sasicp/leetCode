from operator import index


class Solution:
    def partitionString(self, s: str) -> list[str]:
        partitions = []
        part_set = set()
        index = 0
        current_seq = ''
        while index < len(s):
            current_seq += s[index]
            if current_seq not in partitions:
                part_set.add(current_seq)
                partitions.append(current_seq)
                current_seq = ''
            index += 1
        return partitions


if __name__ == '__main__':
    s = Solution()
    print(s.partitionString("aaaccdd"))
    print(s.partitionString("aabcd"))
    print(s.partitionString("aaaa"))
    print(s.partitionString("abbccccd"))
