import os
import answer

try:
    testDataPath = os.environ.get('TestDataPath')
    f = open(testDataPath)
    args = f.readlines()
    newArgs = []
    for arg in args:
        arg = arg.strip().replace('\"', '')
        # Handle quotation marks and carriage returns.
        newArgs.append(arg)
    args = newArgs
    funcName = dir(answer.Solution)[-1]
    if len(args) == 1:
        print(getattr(answer.Solution, funcName)('', args[0]))
    elif len(args) == 2:
        print(getattr(answer.Solution, funcName)('', args[0], args[1]))
    elif len(args) == 3:
        print(getattr(answer.Solution, funcName)('', args[0], args[1], args[2]))
except FileNotFoundError:
    pass
