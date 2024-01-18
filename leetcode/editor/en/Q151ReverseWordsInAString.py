class Solution:
    # 1.remove the extra white spaces
    # 2.reverse the whole string
    # #3.reverse every word
    def reverseWords(self, s: str) -> str:
        pass

    def removeWhiteSpaces(self, s: str):
        lt = list(s)
        # wind up the project
        i, j = 0, 0
        for j in range(len(lt)):
            while lt[j] != ' ':
                lt[i] = lt[j]
                i += 1
            lt[i] = ' '
            i += 1
        return ''.join(lt)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeWhiteSpaces('wind up the project'))
