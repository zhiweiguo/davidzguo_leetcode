# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        self._reverse(s, 0, n-1)
        self._reverse(s, n, len(s)-1)
        self._reverse(s, 0, len(s)-1)
        return ''.join(s)

    def _reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


