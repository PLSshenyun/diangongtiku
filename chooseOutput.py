## 这是导出答题记录的内容

# 导入题库文件
chooseQuestionFile = open("./questions/choose.csv" , "r")
chooseQuestionFileInput = chooseQuestionFile.readlines()
chooseQuestionFile.close()

# 将题库文件导入为字典格式
chooseQuestionDict = dict()
for chooseQuestionFileInputLine in chooseQuestionFileInput:
    chooseQuestionFileInputLineList = chooseQuestionFileInputLine.strip("\n").split(",")
    CQFILL = chooseQuestionFileInputLineList
    chooseQuestionDict[CQFILL[0]] = [CQFILL[0],CQFILL[1],CQFILL[2],CQFILL[3],CQFILL[4],CQFILL[5],CQFILL[6]]

# 导入做题记录
chooseAnswerFile = open("./data/chooseAnswer.sy" , "r")
chooseAnswerFileInput = chooseAnswerFile.read()
chooseAnswerFile.close()

# 将作题记录处理成列表格式
chooseAnswerList = list()
chooseAnswerFileInputList = chooseAnswerFileInput.split(",")
for chooseAnswerFileInputListLine in chooseAnswerFileInputList:
    chooseAnswerFileInputListLineList = chooseAnswerFileInputListLine.split("-")
    chooseAnswerList.append(chooseAnswerFileInputListLineList)

# 缩略词
CQD = chooseQuestionDict
CAL = chooseAnswerList

# 把题库文件和作题记录相互比对，把相同的内容把题库的内容和答题的内容放到一个列表里
answerHistory = list()
for chooseAnswerListLine in chooseAnswerList:
    CALL = chooseAnswerListLine
    answerHistoryline = [CQD[CALL[0]][0],CQD[CALL[0]][1],CQD[CALL[0]][2],CQD[CALL[0]][3],CQD[CALL[0]][4],CQD[CALL[0]][5],CQD[CALL[0]][6],CALL[1],CALL[2]]
    answerHistory.append(answerHistoryline)

# 导出自己的答题记录
import time
name = time.ctime().replace(" ","-").replace(":","-") 
historyOutput = open("./history/{}-choose.csv".format(name) , "w")
historyOutput.write("题号,题目,选项A,选项B,选项C,选项D,正确答案,你的答案,结果\n")
for answerHistoryOutputLine in answerHistory:
    answerHistoryOutputLineStr = ",".join(answerHistoryOutputLine)
    answerHistoryOutputLineStr = answerHistoryOutputLineStr + "\n"
    historyOutput.write(answerHistoryOutputLineStr)
historyOutput.close()
