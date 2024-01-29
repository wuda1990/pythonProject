class Solution:
    # 1.remove the extra white spaces
    # 2.reverse the whole string
    # #3.reverse every word
    def reverseWords(self, s: str) -> str:
        lt = self.removeWhiteSpaces(s)
        lt = lt[::-1]
        i, j = 0, 0
        length = len(lt)
        while j < length:
            if lt[j] == ' ':
                lt[i:j] = lt[i:j][::-1]
                i = j + 1
            j = j + 1
        # process the suffix
        lt[i:j] = lt[i:j][::-1]
        return "".join(lt)

    def removeWhiteSpaces(self, s: str):
        lt = list(s)
        length = len(lt)
        # wind up the project
        i, j = 0, 0
        while j < length:
            if s[j] != ' ':
                if i != 0:
                    lt[i] = ' '
                    i += 1
                while j < length and not lt[j].isspace():
                    lt[i] = lt[j]
                    i += 1
                    j += 1
            j += 1
        return lt[:i]

    def reverseWords2(self, s: str) -> str:
        s = s.strip()
        s = s[::-1]
        s = ''.join(word[::-1] + ' ' for word in s.split())
        return s

    def reverseWords3(self, s: str) -> str:
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords2('wind  up'))
    # print(solution.reverseWords('wind  up'))
# print(solution.reverseWords('wind  up'))
