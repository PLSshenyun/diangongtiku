import os
os.system("python key.py")

inputFile = open("./setting/main.key" , "r")
inputKey = inputFile.read()
inputFile.close()
if inputKey == "True":
    # 选择答题方式
    while True:
        print("今天你要做什么题目呢？")
        print("A：选择题\nB：填空题\n\n")
        userInput = input("请输入：")
        if userInput in "aA":
            userInput = "A"
            break
        elif userInput in "bB":
            userInput = "B"
            break
        else:
            print("你输入的内容有误，你输入的是{}请重新输入！".format(userInput))

    #选择答题方式
    import os
    if userInput == "A":
        os.system("python findChooseQuestion.py")
        os.system("python chooseQuestion.py")
    else:
        os.system("python findJudgeQuestion.py")
        os.system("python judgeQuestion.py")
