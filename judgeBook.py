## 这是选择题的题库本程序

#导入 chooseData.csv 文件
chooseDataFile = open("./data/JudgeData.csv" , "r")
chooseDataInput = chooseDataFile.readlines()
chooseDataFile.close()

#将题库文件处理为字典格式
chooseDataDict = dict()
for chooseDataInputLine in chooseDataInput:
    chooseDataInputLine = chooseDataInputLine.strip("\n")
    chooseDataInputList = chooseDataInputLine.split(",")
    CDIL = chooseDataInputList
    chooseDataDict[CDIL[0]] = CDIL[1]

#导入 chooseAnswer.sy 文件
chooseAnswerFile = open("./data/judgeAnswer.sy" , "r")
chooseAnswerInput = chooseAnswerFile.read()
chooseAnswerFile.close()

#处理题库文件
chooseAnswerList = list()
chooseAnswerInputList = chooseAnswerInput.split(",")
for chooseAnswerInputListLine in chooseAnswerInputList:
    chooseAnswerInputListLineList = list()
    chooseAnswerInputListLineList = chooseAnswerInputListLine.split("-")
    chooseAnswerList.append(chooseAnswerInputListLineList)

#对比题库，替换内容
for chooseAnswerListLine in chooseAnswerList:
    chooseDataDict[chooseAnswerListLine[0]] = chooseAnswerListLine[2]

#将题库处理导出
chooseDataFile = open("./data/judgeData.csv" , "w")
chooseDataDictItems = chooseDataDict.items()
for chooseDataDictItemsLine in chooseDataDictItems:
    chooseDataOutputLine = "{},{}\n".format(chooseDataDictItemsLine[0],chooseDataDictItemsLine[1])
    chooseDataFile.write(chooseDataOutputLine)
chooseDataFile.close()
