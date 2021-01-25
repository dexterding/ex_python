"""
首先，我们要清楚 NLP 任务的基本步骤，也就是下面的四步：
读取文件；
去除所有标点符号和换行符，
并把所有大写变成小写；
合并相同的词，
统计每个词出现的频率，
并按照词频从大到小排序；
将结果按行输出到文件 out.txt。

"""
import os
import re


with open("D:\webdriver\ex_python\in.txt","r") as f:
     text = f.read()

def exe_txt(text):
    text = text.strip() #去除首尾的空格
    text = text.lower() #切换为小写
    #去掉符号和换行符
    text_split = re.split("\n| ",text)

    # 去掉空的元素
    text_split_not = list(filter(None,text_split))


    cou_num = {}
    num = 0
    for word in text_split_not:
        if word not in cou_num:
            cou_num[word] = 0
        cou_num[word] += 1

    # 按照词频排序
    sored_cout = sorted(cou_num.items(),key=lambda x:x[1],reverse=True)
    type(cou_num)
    return sored_cout


freq_txt = exe_txt(text)
print(type(freq_txt))

# with open("D:\webdriver\ex_python\out.txt","w") as out:
#     out.write(freq_txt)
#     # for wo,va in freq_txt:
#         # out.write("{} {}\n".format(wo,va))