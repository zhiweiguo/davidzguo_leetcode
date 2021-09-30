class Solution:
    def replaceSpace(self, s: str) -> str:
        new_s = []
        prefix = '%20'
        for c in s:
            if c != ' ':
                new_s.append(c)
            else:
                new_s.append(prefix)
        return ''.join(new_s)
        