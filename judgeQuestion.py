#打开 question.sy 文件
questionFile = open("./data/judge.sy" , "r")
questionsNumber = questionFile.read()
questionFile.close()

#打开题库 choose.csv 文件
questionFile = open("./questions/judge.csv" , "r")
questionList = questionFile.readlines()
questionFile.close

#显示题目函数
def showQuestions(inputNumber):
    oQ = questionList[eval(inputNumber) - 1]
    oQ = oQ.strip("\n").split(",")
    print("{}. {}\n".format(oQ[0] , oQ[1]))

#转换答案函数
def getAnswer(inputAnswer):
    while(True):
        if inputAnswer == "exit" or inputAnswer == "e":
            return "exit"
        elif inputAnswer in "TF":
            return inputAnswer
        elif inputAnswer == "t":
            return "T"
        elif inputAnswer == "f":
            return "F"
        else:
            print("输入内容错误！你输入的是{}，请重新检查答案！\n".format(inputAnswer))
            inputAnswer = input("你的答案：")

#获得答案函数
def getKey(inputAnswerNumber):
    answerLine = questionList[eval(inputAnswerNumber)-1].strip("\n").split(",")
    answerKey = answerLine[2]
    return answerKey

#对应题目
questionsNumberList = questionsNumber.strip("\n").split(",")

#题目记录器
trueCount = 0
falseCount = 0
questionCount = 0

#答题记录
answeredQuestion = list()

#开始答题
for questionsNumberLine in questionsNumberList:
    showQuestions(questionsNumberLine)
    answer = getAnswer(input("你的答案："))
    #对答案模式
    if answer == "exit":
        break
    elif answer == getKey(questionsNumberLine):
        print("\n回答正确！\n")
        answeredQuestion.append("{}-{}-True".format(eval(questionsNumberLine),answer))
        trueCount += 1
    else:
        print("\n回答错误！正确答案{}\n".format(getKey(questionsNumberLine)))
        falseCount += 1
        answeredQuestion.append("{}-{}-False".format(eval(questionsNumberLine),answer))
    questionCount += 1

print("答题结束，共答{}题，正确{}题，错误{}题，正确率{}".format(questionCount,trueCount,falseCount,trueCount/questionCount))

#导出答题程序
errorOutput = open("./data/judgeAnswer.sy" , "w")
errorOutput.write(",".join(answeredQuestion))
errorOutput.close()

#导出题库
import os
os.system("python judgeBook.py")
os.system("python judgeOutput.py")

#记录答题时间
import time
print("你已经答完所有题目，5秒后自动退出程序……")
time.sleep(5)
