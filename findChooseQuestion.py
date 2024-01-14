# 导入答题记录
inputDataFile = open("./data/chooseData.csv" , "r")
inputDataUnedit = inputDataFile.readlines()
inputDataFile.close()

# 记录题目数量
countNumber = len(inputDataUnedit)

# 将题目数量处理成可用列表
inputData = list()
for inputDataUneditLine in inputDataUnedit:
    inputData.append(inputDataUneditLine.strip("\n").split(","))

# 统计错题题号，未答题题号
wrongQuestion = list()
noneQuestion = list()
for inputDataLine in inputData:
    if inputDataLine[1] == "False":
        wrongQuestion.append(eval(inputDataLine[0]))
    elif inputDataLine[1] == "None":
        noneQuestion.append(eval(inputDataLine[0]))

## 出题姬（咩~）
        
# 出未答的题目 - 数量
def NoAnswerNum(NoAnswerNumber = 0):

    #检查出题数量
    if NoAnswerNumber > 0: #出题数量
        NoAnswerOutput = noneQuestion[0:NoAnswerNumber]
        return NoAnswerOutput
    else:
        NoAnswerOutput = noneQuestion
        return NoAnswerOutput

# 出未答的题目 - 随机
def NoAnswerRandom(NoAnswerRandomNum = 0):
    import random
    RandomNumbers = list()
    
    #检查出题数量
    if NoAnswerRandomNum > 0:
        for NoAnswerRandomNumLine in range(0,NoAnswerRandomNum):
            while(True):
                RandomNumbersLine = random.randint(0,len(noneQuestion))+1
                if not RandomNumbersLine+1 in RandomNumbers:
                    RandomNumbers.append(RandomNumbersLine)
                    break
    else:
        for NoAnswerRandomNumLine in range(0,len(noneQuestion)):
            while(True):
                RandomNumbersLine = random.randint(0,len(noneQuestion))+1
                if not RandomNumbersLine+1 in RandomNumbers:
                    RandomNumbers.append(RandomNumbersLine)
                    break
    return RandomNumbers

# 错误题目 - 数量
def WrongAnswerNum(NoAnswerNumber = 0):

    #检查出题数量
    if NoAnswerNumber > 0: #出题数量
        NoAnswerOutput = wrongQuestion[0:NoAnswerNumber]
        return NoAnswerOutput
    else:
        NoAnswerOutput = wrongQuestion
        return NoAnswerOutput

# 错误的题目 - 随机
def WrongAnswerRandom(NoAnswerRandomNum = 0):
    import random
    RandomNumbers = list()
    
    #检查出题数量
    if NoAnswerRandomNum > 0:
        for NoAnswerRandomNumLine in range(0,NoAnswerRandomNum):
            while(True):
                RandomNumbersLine = random.randint(0,len(wrongQuestion))+1
                if not RandomNumbersLine+1 in RandomNumbers:
                    RandomNumbers.append(RandomNumbersLine+1)
                    break
    else:
        for NoAnswerRandomNumLine in range(0,len(wrongQuestion)):
            while(True):
                RandomNumbersLine = random.randint(0,len(wrongQuestion))+1
                if not RandomNumbersLine+1 in RandomNumbers:
                    RandomNumbers.append(RandomNumbersLine+1)
                    break
    return RandomNumbers

# 选择答题模式
while(True):
    print("欢迎来到出题姬主页面：")
    print("未答题有{}道 / 错题有{}道".format(len(noneQuestion),len(wrongQuestion)))
    print("请选择你的答题模式……\n")
    print("A：答错题（顺序）\nB：答错题（随机）\nC：答未回答题目（顺序）\nD：答未回答题目（随机）\n")
    userInput = input("请输入你的选择（大写字母）：")

    if userInput == "A" or userInput == "a":
        userInput = "A"
        break
    elif userInput == "B" or userInput == "b":
        userInput = "B"
        break
    elif userInput == "C" or userInput == "c":
        userInput = "C"
        break
    elif userInput == "D" or userInput == "d":
        userInput = "D"
        break
    else:
        print("输入错误！你输入的是{}，请按提示输入！\n\n\n".format(userInput))

# 获得答题数量
while(True):
    print("\n请输入要答题的数量！（答所有题则输入数字0）")
    print("未答题有{}道 \t 错题有{}道".format(len(noneQuestion),len(wrongQuestion)))
    userInputNum = input("请输入数字：")
    userInputNum = eval(userInputNum)
    if userInput in "AB":
        if userInputNum <= len(wrongQuestion):
            break
        else:
            print("数字太大\n\n")
    else:
        if userInputNum <= len(noneQuestion):
            break
        else:
            print("数字太大\n\n")

# 生成题目的数字
if userInput == "A":
    questionNumbers = WrongAnswerNum(userInputNum)
elif userInput == "B":
    questionNumbers = WrongAnswerRandom(userInputNum)
elif userInput == "C":
    questionNumbers = NoAnswerNum(userInputNum)
else:
    questionNumbers = NoAnswerRandom(userInputNum)

#导出题库
outputFile = open("./data/choose.sy" , "w")
if len(questionNumbers) == 1:
    outputFile.write(str(questionNumbers[0]))
else:
    questionNumbersList = list()
    for questionNumbersLine in questionNumbers:
        questionNumbersList.append(str(questionNumbersLine))
    outputFile.write(",".join(questionNumbersList))
outputFile.close()
