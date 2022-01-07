class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass

try:
    testDataPath = r'A:\testData.txt'
    f = open(testDataPath)
    # args = tuple(f.readlines())
    args = f.readline().split()
    funcName = dir(Solution)[-1]
    if len(args) == 1:
        print(getattr(Solution, funcName)('', args[0], args[1]))
    if len(args) == 2:
        print(getattr(Solution, funcName)('', args[0], args[1]))
except FileNotFoundError:
    pass
