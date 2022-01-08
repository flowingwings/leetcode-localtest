# LeetCode Local Test Tool
This little tool assists to write and test your code locally when you are solving problems with Python on [LeetCode](leetcode.com).

中文版说明在[这里](github.com/flowingwings/leetcode-localtest/blob/master/说明.md)。

## Background

When doing exercises on LeetCode, I encountered several difficulties:

- Hard to debug on the website without premium.
- Hard to run and test codes locally, because the template LeetCode gives can't be run directly, and the formats of input and the name of the function vary a lot, which means if you test your code using
  ```
  arg1, arg2 = input().split()
  print(Solution.func(arg1, arg2))
  ```
  , you need to modify the function name and arguments and paste the input often. 
- Even after you test your code in the way described above, you can't just `Ctrl`+`A`, `Ctrl`+`C` and `Ctrl`+`V` to submit your answer. This is not cool.

So I tried to develop a little tool to make it that I can write my code in a single file, with the input written locally only once, the testing only needing running a script.
## Usage
This part is based on Pycharm. Other IDEs should be able to do similar things.
1. ~~Setting up a Python run/debug configuration.~~
2. ~~Setting an environment variable whose name is `TestDataPath` and whose value is the path of a local file, in which you will paste the test data. This can be done in system settings or within Pycharm: Run -> Edit Configurations... -> Configuration -> Environment Variables.~~
I have already uploaded the configuration as a `.xml` file, so no need to set it by yourself now. You only need to use the `LeetCodeTest` configuration.
3. Just write and test your code and debug in `answer.py` in this project. Feel free to select all, copy and paste between LeetCode's template and this file.
4. When clicked, the input sample LeetCode gives would select all lines with quotation marks and carriage returns automatically. Just copy it and paste it in your test data file. The script will handle them properly.
5. When submitting the answer, you can just `Ctrl`+`A`, `Ctrl`+`C` and `Ctrl`+`V`.
   
## Disadvantages
This project has too many flaws that I don't know how to make up. The following is part of them.

- This tool doesn't adapt to languages other than Python.
- If you are to add more functions into the class `Solution`, remember to place them in front of the function required by the problem, because I get the function name using
  `funcName = dir(answer.Solution)[-1]`. (Does the order really matter?)
- The ability to deal with input of different kinds or amounts is very weak. Now I can only handle strings as input, and the way to deal with input of different amounts is ugly and unreliable. 