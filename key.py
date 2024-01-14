# 导入 main.key 文件
inputKeyFile = open("./setting/main.key" , "r")
inputKey = inputKeyFile.read()
inputKeyFile.close()

# 序列号生成器
import time
todayTime = time.ctime()
todatTimeList = todayTime.split(" ")
todayTimeStr = "{}{}{}".format(todatTimeList[0],todatTimeList[1],todatTimeList[2])
key = ""
for todayTimeStrLine in todayTimeStr:
    key = key + (chr(ord(todayTimeStrLine)+1))

if inputKey == "False":
    print("你未注册该软件，请输入软件序列号：")
    inputKey = input("在此输入序列号：")
    if inputKey == key:
        print("该序列号已失效，欢迎使用本软件！")

        outputKeyFile = open("./setting/main.key" , "w")
        outputKeyFile.write("True")
        outputKeyFile.close()
    else:
        print("输入序列号错误！即将关闭本软件……")
        time.sleep(5)
