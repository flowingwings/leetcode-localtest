# https://leetcode.com/problems/regular-expression-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            if p[0] == '.':
                return len(s) == 1
            return s == p
        if len(s) == 0:
            if p[1] != '*':
                return False
            return Solution.isMatch('', s, p[2:])
        if p[1] == '*':
            r = range(len(s)+1)
            for i in r:
                if Solution.isMatch('', s[i:], p[2:]):
                    return True
                if i < len(s) and not Solution.isMatch('', s[i], p[0]):
                    break
            return False
        return Solution.isMatch('', s[0], p[0]) and Solution.isMatch('', s[1:], p[1:])
